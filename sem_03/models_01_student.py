from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
    

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self): # информация для вывода
        return f'Student({self.firstname} {self.lastname})'
    
    
class Gender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10), nullable=False, unique=True)
    student = db.relationship(Student, backref=db.backref('gender'), lazy=True) # Обратная связь с student
    
    def __repr__(self): # информация для вывода
        return self.gender
    
    
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty = db.Column(db.String(80), nullable=False, unique=True)
    student = db.relationship(Student, backref=db.backref('faculty'), lazy=True) # Обратная связь с student
    
    def __repr__(self): # информация для вывода
        return self.faculty
    
    
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(80), nullable=False, unique=True)
    student = db.relationship(Student, backref=db.backref('group'), lazy=True) # Обратная связь с student
    
    def __repr__(self): # информация для вывода
        return self.group