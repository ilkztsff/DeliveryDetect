from aiogram.filters.callback_data import CallbackData

from deliverydetect.core.enums import Role


class RoleCallback(CallbackData, prefix='role'):
    role: Role
