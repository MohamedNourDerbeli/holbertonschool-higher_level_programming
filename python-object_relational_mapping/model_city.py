#!/usr/bin/python3
"""
This script defines a City class
to work with MySQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    This is the City class that represents a
    city in the database.
    """

    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
