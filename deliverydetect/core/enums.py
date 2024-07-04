from enum import Enum


class Role(str, Enum):
    COURIER = 'courier'
    CUSTOMER = 'customer'


class Transport(str, Enum):
    FEET = 'feet'
    BIKE = 'bike'
    CAR = 'car'
    MOTORBIKE = 'MOTORBIKE'


class CourierMenuState(str, Enum):
    NAME = 'name'
    CONTACT = 'contact'
    HAS_THERMAL_BAG = 'has_thermal_bag'
    TRANSPORT = 'transport'


class Confirmation(str, Enum):
    YES = True
    NO = False


transport = {
    '🚴 Велосипед': Transport.BIKE,
    '🚘 Автомобиль': Transport.CAR,
    '🏍 Мотоцикл': Transport.MOTORBIKE,
    '🧍 Я хожу пешком': Transport.FEET
}

confirmation = {
    '✅ Да': True,
    '❌ Нет': False
}
