#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
#from models.place import place_amenity
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


if storage_type == "db":
    from models.place import place_amenity
    class Amenity(BaseModel, Base):
        """Amenity class"""
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", back_populates="amenities",
                                       secondary=place_amenity)
else:
    class Amenity(BaseModel):
        name = ""
