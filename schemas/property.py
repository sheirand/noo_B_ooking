from typing import TYPE_CHECKING

from pydantic import BaseModel
import enum


if TYPE_CHECKING:
    from schemas.reservation import Reservation # noqa


class PropertyType(enum.Enum):
    hotel: str = "Hotel"
    hostel: str = "Hostel"
    apartment: str = "Apartment"
    homestay: str = "Homestay"


class PropertyBase(BaseModel):
    title: str
    type: PropertyType
    description: str | None
    price: int
    country: str
    city: str


class PropertyCreate(PropertyBase):
    pass


class Property(PropertyBase):
    id: int
    owner_id: int
    reservations: list[Reservation] = []

    class Config:
        orm_mode = True
