from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

from questions.models import Question

class QuestionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    body = TextAreaField('Body', validators=[DataRequired()])
    image = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post Question')

    def validate_title(self, title):
        question = Question.query.filter_by(title=title.data).first()
        if question:
            raise ValidationError('Title already exists. Please choose a different title.')