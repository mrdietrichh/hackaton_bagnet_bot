from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Для отправки HTTP запросов в API ASP.NET

def create_inline_keyboard(buttons):
    keyboard = InlineKeyboardBuilder()
    for button in buttons:
        keyboard.add(types.InlineKeyboardButton(text=button['text'], callback_data=button['callback_data']))
    return keyboard


kbn = create_inline_keyboard([{'text': 'Назад', 'callback_data': 'back'}])

kbn1 = create_inline_keyboard([{'text': 'Назад', 'callback_data': 'back1'}])

kbn2 = create_inline_keyboard([{'text': 'Назад', 'callback_data': 'back2'}])

kbn3 = create_inline_keyboard([{'text': 'Назад', 'callback_data': 'back3'}])

main_menu_buttons = [
    {'text': 'Мои вопросы', 'callback_data': 'my_vopr'},
    {'text': 'Мои ответы', 'callback_data': 'my_otv'},
    {'text': 'Общий рейтинг', 'callback_data': 'my_score'},
    {'text': 'Форум', 'callback_data': 'my_vopr'},
]

kb0 = create_inline_keyboard(main_menu_buttons)

forum_buttons = [
    {'text': 'Задать вопрос', 'callback_data': 'vopr'},
    {'text': 'Ответить на вопрос', 'callback_data': 'otv'},
    {'text': 'Назад', 'callback_data': 'back'},
]
kb1 = create_inline_keyboard(forum_buttons)

kb2_buttons = [
    {'text': 'Математика', 'callback_data': 'v_mat'},
    {'text': 'Физика', 'callback_data': 'v_fiz'},
    {'text': 'Информ', 'callback_data': 'v_inf'},
    {'text': 'Назад', 'callback_data': 'back1'},
]
kb2 = create_inline_keyboard(kb2_buttons)

kb3_buttons = [
    {'text': 'Математика', 'callback_data': 'mat'},
    {'text': 'Физика', 'callback_data': 'fiz'},
    {'text': 'Информатика', 'callback_data': 'inf'},
    {'text': 'Назад', 'callback_data': 'back'},
]
kb3 = create_inline_keyboard(kb3_buttons)
