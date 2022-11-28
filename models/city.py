#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type
from sqlalchemy.orm import relationship

if storage_type == 'db':
    class City(BaseModel, Base):
        """ the city class, contains state id and name"""
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        # places = relationship("Place", backref="cities")
else:
    class City(BaseModel):
        """ the city class, contains state id and name"""
        state_id = ""
        name = ""
