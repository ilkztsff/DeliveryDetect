from enum import Enum
from deliverydetect.core.settings import _


class Role(str, Enum):
    COURIER = 'courier'
    CUSTOMER = 'customer'


class Transport(str, Enum):
    FEET = _('feet')
    BIKE = _('bike')
    CAR = _('car')
    MOTORBIKE = _('MOTORBIKE')


class CourierMenuState(str, Enum):
    NAME = 'name'
    CONTACT = 'contact'
    HAS_THERMAL_BAG = 'has_thermal_bag'
    TRANSPORT = 'transport'
