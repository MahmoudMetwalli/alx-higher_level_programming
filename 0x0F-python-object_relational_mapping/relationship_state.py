#!/usr/bin/python3
"""Lists states"""

from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship, backref


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
