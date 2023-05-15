import datetime

from pydantic import BaseModel


class ReservationBase(BaseModel):
    num_guests: int
    start_date: datetime.date
    end_date: datetime.date
    property_id: int


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    guest_id: int
    property_id: int

    class Config:
        orm_mode = True
