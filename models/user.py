from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from models.property import Property # noqa
    from models.reservation import Reservation # noqa


class User(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(350), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    property = relationship("Property", back_populates="owner")
    reservations = relationship("Reservation", back_populates="guest")
