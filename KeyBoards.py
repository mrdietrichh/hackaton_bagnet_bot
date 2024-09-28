from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
# Для отправки HTTP запросов в API ASP.NET


kbn = InlineKeyboardBuilder()
kbn.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))

kbn1 = InlineKeyboardBuilder()
kbn1.add(types.InlineKeyboardButton(text="Назад", callback_data="back1"))

kbn2 = InlineKeyboardBuilder()
kbn2.add(types.InlineKeyboardButton(text="Назад", callback_data="back2"))

kbn3 = InlineKeyboardBuilder()
kbn3.add(types.InlineKeyboardButton(text="Назад", callback_data="back3"))

kb0 = InlineKeyboardBuilder()
kb0.add(types.InlineKeyboardButton(text="Вопросы", callback_data="my_vopr"))
kb0.add(types.InlineKeyboardButton(text="Ответы", callback_data="my_otv"))
kb0.add(types.InlineKeyboardButton(text="Баллы", callback_data="my_score"))
kb0.add(types.InlineKeyboardButton(text="Форум", callback_data="forum"))

kb1 = InlineKeyboardBuilder()
kb1.add(types.InlineKeyboardButton(text="Задать", callback_data="vopr"))
kb1.add(types.InlineKeyboardButton(text="Ответить", callback_data="otv"))
kb1.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))

kb2 = InlineKeyboardBuilder()
kb2.add(types.InlineKeyboardButton(text="Матем", callback_data="v_mat"))
kb2.add(types.InlineKeyboardButton(text="Физ", callback_data="v_fiz"))
kb2.add(types.InlineKeyboardButton(text="Информ", callback_data="v_inf"))
kb2.add(types.InlineKeyboardButton(text="Назад", callback_data="back1"))

kb3 = InlineKeyboardBuilder()
kb3.add(types.InlineKeyboardButton(text="Мат", callback_data="mat"))
kb3.add(types.InlineKeyboardButton(text="Физ", callback_data="fiz"))
kb3.add(types.InlineKeyboardButton(text="Информ", callback_data="inf"))
kb3.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))