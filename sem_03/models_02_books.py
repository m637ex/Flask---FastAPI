from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)    # название
    publish_year = db.Column(db.Integer, nullable=False) # год издания
    publish_count = db.Column(db.Integer, nullable=False) # количество экземпляров 
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False) # id автора
    
    def __repr__(self): # информация для вывода
        return f'Book({self.title}, {self.author})'
    

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    book = db.relationship(Book, backref=db.backref('author'), lazy=True) # Обратная связь с student
    
    def __repr__(self): # информация для вывода
        return f'{self.firstname} {self.lastname}'
    
    

    