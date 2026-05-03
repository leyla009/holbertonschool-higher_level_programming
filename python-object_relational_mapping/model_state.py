#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states.
    """
    __tablename__ = 'states'

    # id: auto-generated, unique integer, can't be null, primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # name: string with max 128 characters, can't be null
    name = Column(String(128), nullable=False)
