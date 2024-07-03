from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


choose_role_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я заказчик', callback_data='courier')],
    [InlineKeyboardButton(text='Я курьер', callback_data='customer')]
])
