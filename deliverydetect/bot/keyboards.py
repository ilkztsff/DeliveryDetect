from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from deliverydetect.models.callback import RoleCallback, EditCourierInfoMenuCallback, TransportCallback, ConfirmationCallback
from deliverydetect.core.enums import Role, CourierMenuState, Transport
from deliverydetect.core.settings import _


choose_role_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я заказчик', callback_data=RoleCallback(role=Role.CUSTOMER).pack())],
    [InlineKeyboardButton(text='Я курьер', callback_data=RoleCallback(role=Role.COURIER).pack())]
])


yes_no_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Yes', callback_data=ConfirmationCallback(confirm=True).pack())],
        [InlineKeyboardButton(text='❌ No', callback_data=ConfirmationCallback(confirm=False).pack())]
    ]
)

edit_courier_info_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=_('Имя'), callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.NAME).pack())],
    [InlineKeyboardButton(text=_('Телефон'), callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.CONTACT).pack())],
    [InlineKeyboardButton(text=_('Наличие термосумки'), callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.HAS_THERMAL_BAG).pack())],
    [InlineKeyboardButton(text=_('Транспорт'), callback_data=EditCourierInfoMenuCallback(state=CourierMenuState.TRANSPORT).pack())]
])

choose_transport_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=_('🚴 Bike'), callback_data=TransportCallback(transport=Transport.BIKE).pack())],
        [InlineKeyboardButton(text=_('🚘 Car'), callback_data=TransportCallback(transport=Transport.CAR).pack())],
        [InlineKeyboardButton(text=_('🏍 Motorbike'), callback_data=TransportCallback(transport=Transport.MOTORBIKE).pack())],
        [InlineKeyboardButton(text=_('🧍 I\'m going on foot'), callback_data=TransportCallback(transport=Transport.FEET).pack())]
    ]
)
