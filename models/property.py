import enum
from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from models.user import User # noqa


class PropertyType(enum.Enum):
    hotel: str = "Hotel"
    hostel: str = "Hostel"
    apartment: str = "Apartment"
    homestay: str = "Homestay"


class Property(Base):

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    type = Column(Enum(PropertyType))
    description = Column(String)
    price = Column(Integer, index=True)
    country = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="property")
