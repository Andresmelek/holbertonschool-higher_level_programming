#!/usr/bin/python3
"""
class definition of a City  and an instance Base
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


Base = declarative_base()


class City(Base):
    """Class city that inherits from base"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
