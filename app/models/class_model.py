# app/models/class_model.py

from app import db

class ClassModel(db.Model):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    start_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, description, duration, start_time):
        self.name = name
        self.description = description
        self.duration = duration
        self.start_time = start_time

    def __repr__(self):
        return f"<Class {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "start_time": self.start_time.isoformat(),  # convert datetime to string
        }