# app/routes/booking_routes.py

from flask import Blueprint, jsonify, request
from app.models import BookingModel
from app import db

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = BookingModel.query.all()
    return jsonify([booking.to_dict() for booking in bookings]), 200

@booking_bp.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    new_booking = BookingModel(user_id=data['user_id'], class_id=data['class_id'])
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(new_booking.to_dict()), 201

# Additional routes for booking management can be added here.
