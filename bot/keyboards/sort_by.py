from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sort_by_rarity = InlineKeyboardButton(
    text='Sort by rarity',
    callback_data='choicen_sort_by_rarity'
)

sort_by_element = InlineKeyboardButton(
    text='Sort by element',
    callback_data='choicen_sort_by_element'
)

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[sort_by_rarity],
                     [sort_by_element]]
)
