import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
# Для отправки HTTP запросов в API ASP.NET
import requests, json
from KeyBoards import kbn, kb1, kbn2, kb2, kbn1, kbn3, kb0, kb3


logging.basicConfig(level=logging.INFO)
bot = Bot(token="7667356981:AAECXx4Zt0bVOmg7P8iE3O_Qssntdk2_HJg")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Студент " + str(message.from_user.username) + ", Добро Пожаловать!"
                                                                        "\nВы можете узнать:\nКакие вопросы вы задавали ранее,\nНа какие вопросы вы уже ответили,\nСвои баллы за ответы,\nЗадать вопрос или ответить на него",
                         reply_markup=kb0.as_markup())
    us_id = message.from_user.id
    us_n = message.from_user.username

    @dp.callback_query(F.data == 'my_vopr')
    async def m_q(callback: types.CallbackQuery):
        await callback.message.answer("Ожидайте ответ от бд по вашим вопросам", reply_markup=kbn.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'my_otv')
    async def m_a(callback: types.CallbackQuery):
        await callback.message.answer("Ожидайте ответ от бд по вашим ответам", reply_markup=kbn.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'my_score')
    async def m_s(callback: types.CallbackQuery):
        api_url = 'http://localhost:8001/api/Category/get-all'
        # data = {'s': 's'}
        # json_data = json.dump(data)
        # print(json_data)
        # response = requests.post(api_url, data=json_data, headers={'Content-Type': 'application/json'})
        response = requests.get(api_url)
        result = json.loads(response.text)
        if not result['succeeded']:
            await callback.message.answer(f"Произошла ошибка", reply_markup=kbn.as_markup())
            await callback.message.delete()

        category = result['data'][0]
        # ['category_id']

        await callback.message.answer(f"{category['title']}", reply_markup=kbn.as_markup())
        await callback.message.delete()


    @dp.callback_query(F.data == 'forum')
    async def forum(callback: types.CallbackQuery):
        await callback.message.answer("Здесь вы можете задать вопрос или ответить на него:",
                                      reply_markup=kb1.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'back')
    async def back(callback: types.CallbackQuery):
        await message.answer("Студент " + str(message.from_user.username) + ", Добро Пожаловать!"
                                                                            "\nВы можете узнать:\nКакие вопросы вы задавали ранее,\nНа какие вопросы вы уже ответили,\nСвои баллы за ответы,\nЗадать вопрос или ответить на него",
                             reply_markup=kb0.as_markup())
        await callback.message.delete()


@dp.callback_query(F.data == 'vopr')
async def tasks(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса:", reply_markup=kb3.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'mat')
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Введите ваш вопрос:")
    await callback.message.delete()


@dp.callback_query(F.data == 'fiz')
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Введите ваш вопрос:")
    await callback.message.delete()


@dp.callback_query(F.data == 'inf')
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Введите ваш вопрос:")
    await callback.message.delete()


@dp.callback_query(F.data == 'otv')
async def answers(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса, на который хотите ответить:", reply_markup=kb2.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'v_mat')
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Вопросов по выбранному предмету пока не задано", reply_markup=kbn2.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'v_fiz')
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Вопросов по выбранному предмету пока не задано", reply_markup=kbn2.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'v_inf')
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Вопросов по выбранному предмету пока не задано", reply_markup=kbn2.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'back1')
async def forum(callback: types.CallbackQuery):
    await callback.message.answer("Здесь вы можете задать вопрос или ответить на него:", reply_markup=kb1.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'back2')
async def back1(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса, на который хотите ответить:", reply_markup=kb2.as_markup())
    await callback.message.delete()


@dp.callback_query(F.data == 'back3')
async def back1(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса:", reply_markup=kb3.as_markup())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
