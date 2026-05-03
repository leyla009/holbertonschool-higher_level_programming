#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.
    """
    __tablename__ = 'cities'

    # id: auto-generated, unique integer, can't be null, primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # name: string of 128 characters, can't be null
    name = Column(String(128), nullable=False)

    # state_id: integer, can't be null, foreign key to states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
