# app/utils/helpers.py

from datetime import datetime

def format_datetime(value, format='%Y-%m-%dT%H:%M:%S'):
    """Format a datetime object to a string"""
    if value is None:
        return None
    return value.strftime(format)
