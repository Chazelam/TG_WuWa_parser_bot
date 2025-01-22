from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from bot.keys import BOT_TOKEN
from bot.functions import update_characters_list, load_data_base
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.keyboards.sort_by import *
from bot.keyboards.choice_rarity import *
from bot.keyboards.choice_element import *

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7',}

# Функция для генерации инлайн-клавиатур "на лету"
def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    keyboard = create_inline_kb(2, **load_data_base())
    await message.answer(
        text='Это инлайн-клавиатура, сформированная функцией '
             '<code>create_inline_kb</code>',
        reply_markup=keyboard
    )







# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'choicen_sort_by_rarity')
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Choce rarity of resonator:',
        reply_markup=star_selector_keyboard
    )

# Этот хэндлер будет срабатывать на апдейт типа CallbackQuery
# с data 'big_button_1_pressed'
@dp.callback_query(F.data == 'choicen_sort_by_element')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Choce element of resonator:',
        reply_markup=element_sort_keyboard
    )

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/updatebase"
@dp.message(Command(commands=['updatebase']))
async def process_help_command(message: Message):
    update_characters_list()
    await  message.reply(text="Done")



@dp.message(Command(commands=['characterlist']))
async def process_hep_command(message: Message):
    # char_list = load_data_base()
    await message.answer(
        text='Это инлайн-кнопки. Нажми на любую!',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)