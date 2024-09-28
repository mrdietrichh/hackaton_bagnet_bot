from aiogram import types
from aiogram import F
from hackaton_bagnet_bot.KeyBoards import kbn, kb1, kbn2, kb2, kbn1, kbn3, kb0, kb3
from hackaton_bagnet_bot.ManagerAPI.get_request import get_response, deserializer


async def handle_my_vopr(callback: types.CallbackQuery):
    await callback.message.answer("Ожидайте ответ от БД по вашим вопросам", reply_markup=kbn.as_markup())
    await callback.message.delete()


async def handle_my_otv(callback: types.CallbackQuery):
    await callback.message.answer("Ожидайте ответ от БД по вашим ответам", reply_markup=kbn.as_markup())
    await callback.message.delete()


async def handle_my_score(callback: types.CallbackQuery):
    api_url = 'http://localhost:8001/api/User/get-paginted-by-rating?pageNumber=1&pageSize=10'
    response = get_response(url=api_url)
    result = deserializer(response.text)

    rating_list = result['data']['list']
    output_string = ''
    count = 1

    for item in rating_list:
        output_string += f'{count}. {item["first_name"]} {item["last_name"]}, очков - {item["points_counts"]} \n'
        count += 1

    if not result['succeeded']:
        await callback.message.answer("Произошла ошибка", reply_markup=kbn.as_markup())
        await callback.message.delete()
        return

    await callback.message.answer(output_string, reply_markup=kbn.as_markup())
    await callback.message.delete()


async def handle_forum(callback: types.CallbackQuery):
    await callback.message.answer("Здесь вы можете задать вопрос или ответить на него:", reply_markup=kb1.as_markup())
    await callback.message.delete()


async def handle_back(callback: types.CallbackQuery):
    await callback.message.answer(
        f"Студент {callback.from_user.username}, Добро Пожаловать!"
        "\nВы можете узнать:\nКакие вопросы вы задавали ранее,\nНа какие вопросы вы уже ответили,\nСвои баллы за ответы,\nЗадать вопрос или ответить на него",
        reply_markup=kb0.as_markup()  # Используем клавиатуру с кнопками "форум" и "общий рейтинг"
    )
    await callback.message.delete()


async def handle_vopr(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса:", reply_markup=kb3.as_markup())
    await callback.message.delete()


async def handle_subject_vopr(callback: types.CallbackQuery):
    await callback.message.answer("Введите ваш вопрос:")
    await callback.message.delete()


async def handle_otv(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса, на который хотите ответить:", reply_markup=kb2.as_markup())
    await callback.message.delete()


async def handle_subject_otv(callback: types.CallbackQuery):
    await callback.message.answer("Вопросов по выбранному предмету пока не задано", reply_markup=kbn2.as_markup())
    await callback.message.delete()


def register(dp):
    dp.callback_query.register(handle_my_vopr, F.data == 'my_vopr')
    dp.callback_query.register(handle_my_otv, F.data == 'my_otv')
    dp.callback_query.register(handle_my_score, F.data == 'my_score')
    dp.callback_query.register(handle_forum, F.data == 'forum')
    dp.callback_query.register(handle_back, F.data == 'back')
    dp.callback_query.register(handle_vopr, F.data == 'vopr')
    dp.callback_query.register(handle_subject_vopr, F.data.in_(['mat', 'fiz', 'inf']))  # Темы для вопросов
    dp.callback_query.register(handle_otv, F.data == 'otv')
    dp.callback_query.register(handle_subject_otv, F.data.in_(['v_mat', 'v_fiz', 'v_inf']))  # Темы для ответов
    dp.callback_query.register(handle_back, F.data == 'back1')
    dp.callback_query.register(handle_back, F.data == 'back2')
    dp.callback_query.register(handle_back, F.data == 'back3')
