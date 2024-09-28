import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import requests
import json
from KeyBoards import kbn, kb1, kbn2, kb2, kbn1, kbn3, kb0, kb3
from settings import config
from ManagerAPI.get_request import *

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    api_url = 'http://localhost:8001/api/User/add-telegram-user'
    us_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    data = {
        "user_id": us_id,
        "first_name": first_name,
        "last_name": last_name,
    }

    # Отправка данных на сервер
    json_data = json.dumps(data)
    requests.post(api_url, data=json_data, headers={'Content-Type': 'application/json'})

    await message.answer(
        f"Студент {message.from_user.full_name}, Добро Пожаловать!"
        "\nВы можете узнать:\nКакие вопросы вы задавали ранее,\nНа какие вопросы вы уже ответили,\nСвои баллы за ответы,\nЗадать вопрос или ответить на него",
        reply_markup=kb0.as_markup()
    )

    # Вызов функции для обработки колбэков
    await setup_callbacks(message)

async def setup_callbacks(message: types.Message):
    @dp.callback_query(F.data == 'my_vopr')
    async def m_q(callback: types.CallbackQuery):
        await callback.message.answer("Ожидайте ответ от БД по вашим вопросам", reply_markup=kbn.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'my_otv')
    async def m_a(callback: types.CallbackQuery):
        await callback.message.answer("Ожидайте ответ от БД по вашим ответам", reply_markup=kbn.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'my_score')
    async def m_s(callback: types.CallbackQuery):
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

    @dp.callback_query(F.data == 'forum')
    async def forum(callback: types.CallbackQuery):
        await callback.message.answer("Здесь вы можете задать вопрос или ответить на него:", reply_markup=kb1.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'back')
    async def back(callback: types.CallbackQuery):
        await message.answer(
            f"Студент {message.from_user.username}, Добро Пожаловать!"
            "\nВы можете узнать:\nКакие вопросы вы задавали ранее,\nНа какие вопросы вы уже ответили,\nСвои баллы за ответы,\nЗадать вопрос или ответить на него",
            reply_markup=kb0.as_markup()
        )
        await callback.message.delete()

# Добавление оставшихся колбэков
@dp.callback_query(F.data == 'vopr')
async def tasks(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса:", reply_markup=kb3.as_markup())
    await callback.message.delete()

@dp.callback_query(F.data.in_(['mat', 'fiz', 'inf']))  # Объединенный обработчик
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Введите ваш вопрос:")
    await callback.message.delete()

@dp.callback_query(F.data == 'otv')
async def answers(callback: types.CallbackQuery):
    await callback.message.answer("Выберите тему вопроса, на который хотите ответить:", reply_markup=kb2.as_markup())
    await callback.message.delete()

@dp.callback_query(F.data.in_(['v_mat', 'v_fiz', 'v_inf']))  # Объединенный обработчик
async def no_questions(callback: types.CallbackQuery):
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
