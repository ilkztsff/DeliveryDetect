from aiogram.fsm.state import State, StatesGroup


class GetCourierInfo(StatesGroup):
    GET_NAME = State()
    GET_CONTACT = State()
    GET_HAS_THERMAL_BAG = State()
    GET_TRANSPORT = State()
