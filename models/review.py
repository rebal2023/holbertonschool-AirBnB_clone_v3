#!/usr/bin/python3
"""
Review Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey # type: ignore
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    if storage_type == "db":
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ''
        user_id = ''
        text = ''