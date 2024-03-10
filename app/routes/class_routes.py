# app/routes/class_routes.py

from flask import Blueprint, jsonify, request
from app.models import ClassModel
from app.services import ClassService
from app.utils.validators import validate_class_data
from app import db



class_bp = Blueprint('class_bp', __name__)


# app.register_blueprint(class_bp, url_prefix='/api/classes')
@class_bp.route('/classes', methods=['GET'])
def get_classes():
    classes = ClassModel.query.all()
    return jsonify([class_.to_dict() for class_ in classes]), 200

@class_bp.route('/classes', methods=['POST'])
def create_class():
    data = request.get_json()
    errors = validate_class_data(data)
    if errors:
        return jsonify({'error': errors}), 400
    new_class = ClassService.create_class(data)
    return jsonify(new_class.to_dict()), 201

# Additional routes like update and delete can be added here.
