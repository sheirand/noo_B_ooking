from typing import TYPE_CHECKING

from pydantic import BaseModel, EmailStr


if TYPE_CHECKING:
    from schemas.reservation import Reservation # noqa
    from schemas.property import Property # noqa


class UserBase(BaseModel):
    email: EmailStr = None
    name: str | None = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = True
    property: list[Property] = []
    reservations: list[Reservation] = []

    class Config:
        orm_mode = True
