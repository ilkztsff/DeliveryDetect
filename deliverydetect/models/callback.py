from aiogram.filters.callback_data import CallbackData
from deliverydetect.core.enums import Role, CourierMenuState


class RoleCallback(CallbackData, prefix='role'):
    role: Role


class EditCourierInfoMenuCallback(CallbackData, prefix='courier'):
    state: CourierMenuState
