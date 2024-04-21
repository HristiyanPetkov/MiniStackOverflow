from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity

from questions.services import *
from questions.models import Question
from questions.forms import QuestionForm
from extensions import db

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route('/new', methods=["GET", "POST"])
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        new_question = Question(
            title=form.title.data,
            body=form.body.data,
            user_id=get_jwt_identity()
        )
        db.session.add(new_question)
        db.session.commit()

        return jsonify({'message': 'Question posted successfully'}), 201
    
    return render_template('new_question.html', form=form)
