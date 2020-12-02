from sqlalchemy import Column, Integer, String, Boolean

from .database import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_done = Column(Boolean, nullable=False, default=False)
