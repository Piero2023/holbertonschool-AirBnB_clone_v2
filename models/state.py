#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


if models.storage_type == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            from models import storage
            objs = [x for x in storage.all().values()
                    if type(x) == City and x.state_id == self.id]
            return objs
            '''new_list = []
            cities_all = models.storage.all(City)
            for value in cities_all.values():
                if (value.state_id == self.id):
                    new_list.append(value)
            return new_list'''
