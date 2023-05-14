from db.base_class import Base
from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Reservation(Base):

    id = Column(Integer, primary_key=True, index=True)
