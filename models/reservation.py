from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from models.user import User # noqa
    from models.property import Property # noqa


class Reservation(Base):

    id = Column(Integer, primary_key=True, index=True)
    num_guests = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    guest_id = Column(Integer, ForeignKey("user.id"))
    guest = relationship("User", back_populates="reservations")
    property_id = Column(Integer, ForeignKey("property.id"))
    property = relationship("Property", back_populates="reservations")
