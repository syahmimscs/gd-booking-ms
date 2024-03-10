# app/utils/validators.py

from datetime import datetime

def validate_class_data(data):
    errors = {}
    if not data.get('name'):
        errors['name'] = 'Class name is required.'
    if not data.get('start_time') or not _is_valid_datetime(data['start_time']):
        errors['start_time'] = 'A valid start time is required.'
    # Add more validations as necessary
    return errors

def validate_booking_data(data):
    errors = {}
    if not data.get('user_id'):
        errors['user_id'] = 'User ID is required.'
    if not data.get('class_id'):
        errors['class_id'] = 'Class ID is required.'
    # Add more validations as necessary
    return errors

def _is_valid_datetime(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
        return True
    except ValueError:
        return False
