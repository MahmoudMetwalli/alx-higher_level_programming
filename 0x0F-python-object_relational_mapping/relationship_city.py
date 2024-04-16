#!/usr/bin/python3
"""To make City object"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base



class City(Base):
    """City class inheriting from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)