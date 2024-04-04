from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
    
    
class Evaluation03(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student03.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson03.id'), nullable=False) # название предмета
    evaluation = db.Column(db.Integer, nullable=False) # оценка
    
    def __repr__(self): # информация для вывода
        return f'{self.evaluation}'
    
    
class Lesson03(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    lesson = db.Column(db.String(80), nullable=False, unique=True) # название предмета
    evaluation03 = db.relationship(Evaluation03, backref=db.backref('lesson'), lazy=True) # Обратная связь с Evaluation
    
    def __repr__(self): # информация для вывода
        return f'{self.lesson}'


# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.

class Student03(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    group_id = db.Column(db.Integer, db.ForeignKey('group03.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    evaluation03 = db.relationship(Evaluation03, backref=db.backref('firstname'), lazy=True) # Обратная связь с Evaluation
    
    def __repr__(self): # информация для вывода
        return f'{self.firstname} {self.lastname}'
    
    
class Group03(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(80), nullable=False, unique=True)
    student03 = db.relationship(Student03, backref=db.backref('group03'), lazy=True) # Обратная связь с student
    
    def __repr__(self): # информация для вывода
        return self.group