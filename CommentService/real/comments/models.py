from extensions import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    publication_ts = db.Column(db.Datetime, nullable=False)
    body = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<Comment {self.title}>"
