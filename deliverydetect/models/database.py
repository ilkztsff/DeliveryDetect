from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

from deliverydetect.core.enums import Transport


Base = declarative_base()


class Courier(Base):
    __tablename__ = 'courier'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    contact: Mapped[str]
    has_thermal_bag: Mapped[bool]
    transport: Mapped[Transport]
