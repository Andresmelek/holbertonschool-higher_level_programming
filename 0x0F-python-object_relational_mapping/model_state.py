#!/usr/bin/python3
"""
class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class state that inherits from base"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
