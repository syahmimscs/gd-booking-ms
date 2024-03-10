# app/services/booking_service.py

from app.models import BookingModel
from app import db

class BookingService:
    
    @staticmethod
    def get_all_bookings():
        return BookingModel.query.all()

    @staticmethod
    def create_booking(user_id, class_id):
        new_booking = BookingModel(user_id=user_id, class_id=class_id)
        db.session.add(new_booking)
        db.session.commit()
        return new_booking

    # Additional business logic related to bookings can go here, such as cancellation of a booking.
