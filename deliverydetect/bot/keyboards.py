from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from deliverydetect.models.callback import RoleCallback
from deliverydetect.core.enums import Role


choose_role_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я заказчик', callback_data=RoleCallback(role=Role.CUSTOMER).pack())],
    [InlineKeyboardButton(text='Я курьер', callback_data=RoleCallback(role=Role.COURIER).pack())]
])
