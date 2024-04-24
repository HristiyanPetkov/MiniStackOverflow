from flask import Blueprint, request, jsonify

from answers.services import *

answers_bp = Blueprint('answers', __name__, url_prefix='/answers')

@answers_bp.route('/create', methods=["POST"])
def create_answer():
    data = request.get_json()
    
    message = create_answer_object(data)

    return jsonify(message), 201

@answers_bp.route('/get_one/<int:answer_id>', methods=["GET"])
def get_answer(answer_id):
    message = get_answer_by_id(answer_id)

    return jsonify(message), 200

@answers_bp.route('/get_all', methods=["GET"])
def get_all():
    message = get_all_answers()
    
    return jsonify(message), 200

@answers_bp.route('/set_final/<int:answer_id>', methods=["PATCH"])
def set_final(answer_id):
    message = set_final_answer_by_id(answer_id)

    return jsonify(message), 200

@answers_bp.route('/is_final/<int:answer_id>', methods=["GET"])
def is_final(answer_id):
    message = is_final_by_id(answer_id)

    return jsonify(message), 200

@answers_bp.route('/delete_one/<int:answer_id>', methods=["DELETE"])
def delete_answer(answer_id):
    message = delete_answer_by_id(answer_id)

    return jsonify(message), 200

@answers_bp.route('/delete_all', methods=["DELETE"])
def delete_all():
    message = delete_all_answers()

    return jsonify(message), 200
