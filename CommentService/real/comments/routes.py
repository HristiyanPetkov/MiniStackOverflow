from flask import Blueprint, request, jsonify

from comments.services import *

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')

@comments_bp.route('/create', methods=["POST"])
def create_comment():
    data = request.get_json()
    
    message = create_comment_object(data)

    return jsonify(message), 201


@comments_bp.route('/get_for_one_answer/<int:answer_id>', methods=["GET"])
def get_comment(answer_id):
    message = get_comments_by_answer_id(answer_id)

    return jsonify(message), 200


@comments_bp.route('/delete_one/<int:comment_id>', methods=["DELETE"])
def delete_comment(comment_id):
    message = delete_comment_by_id(comment_id)

    return jsonify(message), 200


@comments_bp.route('/delete_all', methods=["DELETE"])
def delete_all():
    message = delete_all_comments()

    return jsonify(message), 200