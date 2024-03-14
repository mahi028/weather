from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Key(db.Model):
    __tablename__ = 'keys'
    key_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    key_code = db.Column(db.String, nullable = False, unique = True)