from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
    
    
class User04(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self): # информация для вывода
        return f'{self.name}'
