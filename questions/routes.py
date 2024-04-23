from flask import Blueprint, request, jsonify

from questions.services import *

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route('/create', methods=["POST"])
def create_question():
    data = request.get_json()
    
    create_question(data)

    return jsonify({"message": "Question created successfully"}), 201

@questions_bp.route('/<int:question_id>', methods=["GET"])
def get_question(question_id):
    question = get_question_by_id(question_id)

    return jsonify(question), 200

@questions_bp.route('/<int:question_id>/resolve', methods=["PATCH"])
def resolve_question(question_id):
    question = resolve_question_by_id(question_id)

    return jsonify(question), 200

@questions_bp.route('/<int:question_id>/is_resolved', methods=["GET"])
def is_resolved(question_id):
    question = get_question_by_id(question_id)

    return jsonify({"is_resolved": question.is_resolved}), 200