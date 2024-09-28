import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import requests
import json
from hackaton_bagnet_bot.KeyBoards import kbn, kb1, kbn2, kb2, kbn1, kbn3, kb0, kb3
from hackaton_bagnet_bot.settings import config
from hackaton_bagnet_bot.ManagerAPI.get_request import *
from hackaton_bagnet_bot.ManagerAPI import *


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
        "\nВы можете узнать:\nКакие вопросы вы задавали ранее,"
        "\nНа какие вопросы вы уже ответили,\nСвои баллы за ответы,"
        "\nЗадать вопрос или ответить на него",
        reply_markup=kb0.as_markup()
    )


def register(dp):
    dp.message.register(cmd_start, Command('start'))
