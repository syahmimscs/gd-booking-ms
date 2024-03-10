# app/models/booking_model.py

from app import db

class BookingModel(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    booking_time = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    def __init__(self, user_id, class_id):
        self.user_id = user_id
        self.class_id = class_id

    def __repr__(self):
        return f'<Booking User: {self.user_id}, Class: {self.class_id}>'
