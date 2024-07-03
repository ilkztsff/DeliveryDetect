from enum import Enum


class Role(str, Enum):
    COURIER = 'courier'
    CUSTOMER = 'customer'


class Transport(str, Enum):
    FEET = 'feet'
    BIKE = 'bike'
    CAR = 'car'
    MOTORBIKE = 'MOTORBIKE'
