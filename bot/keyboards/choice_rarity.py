from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

show_five_star = InlineKeyboardButton(
    text='show five star',
    callback_data='choiced_show_five_star'
)

show_four_star = InlineKeyboardButton(
    text='show four star',
    callback_data='choiced_show_four_star'
)

# Создаем объект инлайн-клавиатуры
star_selector_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[show_five_star],
                     [show_four_star]]
)
