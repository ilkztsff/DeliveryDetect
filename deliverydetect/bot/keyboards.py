from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from deliverydetect.models.callback import RoleCallback, EditCourierInfoMenuCallback
from deliverydetect.core.enums import Role, CourierMenuState


choose_role_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я заказчик', callback_data=RoleCallback(role=Role.CUSTOMER).pack())],
    [InlineKeyboardButton(text='Я курьер', callback_data=RoleCallback(role=Role.COURIER).pack())]
])


yes_no_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✅ Да')],
        [KeyboardButton(text='❌ Нет')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)


edit_courier_info_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Имя', callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.NAME).pack())],
    [InlineKeyboardButton(text='Телефон', callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.CONTACT).pack())],
    [InlineKeyboardButton(text='Наличие термосумки', callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.HAS_THERMAL_BAG).pack())],
    [InlineKeyboardButton(text='Транспорт', callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.TRANSPORT).pack())]
])

choose_transport_kb = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text='🚴 Велосипед')],
        [KeyboardButton(text='🚘 Автомобиль')],
        [KeyboardButton(text='🏍 Мотоцикл')],
        [KeyboardButton(text='🧍 Я хожу пешком')]
    ]
)
