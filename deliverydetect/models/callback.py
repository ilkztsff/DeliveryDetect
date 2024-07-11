from aiogram.filters.callback_data import CallbackData
from deliverydetect.core.enums import Role, CourierMenuState, Transport


class RoleCallback(CallbackData, prefix='role'):
    role: Role


class EditCourierInfoMenuCallback(CallbackData, prefix='courier'):
    state: CourierMenuState


class TransportCallback(CallbackData, prefix='transport'):
    transport: Transport


class ConfirmationCallback(CallbackData, prefix='confirmation'):
    confirm: bool
