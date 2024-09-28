import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
logging.basicConfig(level=logging.INFO)
bot = Bot(token="7666590149:AAF75xg0HsEKdZlHRdliRGEGfHWLick6prM")
dp = Dispatcher()

kbn = InlineKeyboardBuilder()
kbn.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back"))

kbn1 = InlineKeyboardBuilder()
kbn1.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back1"))

kbn2 = InlineKeyboardBuilder()
kbn2.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back2"))

kbn3 = InlineKeyboardBuilder()
kbn3.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back3"))

kb0 = InlineKeyboardBuilder()
kb0.add(types.InlineKeyboardButton(text= "Вопросы", callback_data= "my_vopr"))
kb0.add(types.InlineKeyboardButton(text= "Ответы", callback_data= "my_otv"))
kb0.add(types.InlineKeyboardButton(text= "Баллы", callback_data= "my_score"))
kb0.add(types.InlineKeyboardButton(text= "Форум", callback_data= "forum"))

kb1 = InlineKeyboardBuilder()
kb1.add(types.InlineKeyboardButton(text= "Задать", callback_data= "vopr"))
kb1.add(types.InlineKeyboardButton(text= "Ответить", callback_data= "otv"))
kb1.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back"))

kb2 = InlineKeyboardBuilder()
kb2.add(types.InlineKeyboardButton(text= "Матем", callback_data= "v_mat"))
kb2.add(types.InlineKeyboardButton(text= "Физ", callback_data= "v_fiz"))
kb2.add(types.InlineKeyboardButton(text= "Информ", callback_data= "v_inf"))
kb2.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back1"))

kb3 = InlineKeyboardBuilder()
kb3.add(types.InlineKeyboardButton(text= "Мат", callback_data= "mat"))
kb3.add(types.InlineKeyboardButton(text= "Физ", callback_data= "fiz"))
kb3.add(types.InlineKeyboardButton(text= "Информ", callback_data= "inf"))
kb3.add(types.InlineKeyboardButton(text= "Назад", callback_data= "back"))

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
        await callback.message.answer("Ожидайте ответ от бд по вашим баллам", reply_markup=kbn.as_markup())
        await callback.message.delete()

    @dp.callback_query(F.data == 'forum')
    async def forum(callback: types.CallbackQuery):
        await callback.message.answer("Здесь вы можете задать вопрос или ответить на него:", reply_markup=kb1.as_markup())
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