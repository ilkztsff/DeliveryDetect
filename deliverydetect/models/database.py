from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from deliverydetect.core.enums import Transport


class Base(DeclarativeBase):
    pass


class Courier(Base):
    __tablename__ = 'courier'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    contact: Mapped[str]
    has_thermal_bag: Mapped[bool]
    transport: Mapped[Transport]
