# app/services/class_service.py

from app.models import ClassModel
from app import db

class ClassService:
    
    @staticmethod
    def get_all_classes():
        return ClassModel.query.all()

    @staticmethod
    def create_class(data):
        new_class = ClassModel(
            name=data['name'],
            description=data['description'],
            duration=data['duration'],
            start_time=data['start_time']
        )
        db.session.add(new_class)
        db.session.commit()
        return new_class

    # Additional business logic related to classes can go here, like updating or deleting classes.
