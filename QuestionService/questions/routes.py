from flask import Blueprint, request, jsonify

from questions.services import *

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route('/create', methods=["POST"])
def create_question():
    data = request.get_json()
    
    message = create_question_object(data)

    return jsonify(message), 201

@questions_bp.route('/get_one/<int:question_id>', methods=["GET"])
def get_question(question_id):
    message = get_question_by_id(question_id)

    return jsonify(message), 200

@questions_bp.route('/get_all', methods=["GET"])
def get_all():
    message = get_all_questions()
    
    return jsonify(message), 200

@questions_bp.route('/resolve/<int:question_id>', methods=["PATCH"])
def resolve_question(question_id):
    message = resolve_question_by_id(question_id)

    return jsonify(message), 200

@questions_bp.route('/is_resolved/<int:question_id>', methods=["GET"])
def is_resolved(question_id):
    message = is_resolved_by_id(question_id)

    return jsonify(message), 200
