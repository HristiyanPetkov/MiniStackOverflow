from extensions import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=True)
    is_resolved = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"<Question {self.title}>"
