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
from hackaton_bagnet_bot.handlers import callbacks, commands

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

commands.register(dp=dp)
callbacks.register(dp=dp)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
