from extensions import db

class Answer(db.Model):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    is_final = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Answer {self.title}>"
