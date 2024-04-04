# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.


from flask import Flask
from models_03_student import db, Student03, Evaluation03, Group03, Lesson03
from random import randint
from flask import render_template
# pip install faker
from faker import Faker # Faker - это библиотека для генерации случайных данных 
fake = Faker()

app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar-flask-db.db'   # Задаём тип и место БД
db.init_app(app)

@app.route('/') 
def index():     
    return 'Hi!'

@app.route('/evaluation/') 
def all_evaluation():  
    evaluation = Evaluation03.query.all() #обращение к модели  Student, с запросом query на all - всё
    context = {'evaluations': evaluation} # словарь контекста
    return render_template('evaluation.html', **context)


@app.route('/init-db/') 
# @app.cli.command("init-db")  # запуск из командной строки через  flask init-db (нужно изменить пути импорта библиотек!!!)
def init_db():
    db.create_all() # создай таблицы в БД
    print ("init-db 0K")
    return "init-db 0K"


@app.route('/fill-db/') 
# @app.cli.command("fill-db") # ➢Наполнение тестовыми данными (нужно изменить пути импорта библиотек!!!)
def fill_tables():
    count = 10
    # Добавляем Студентов
    for student in range(1, count + 1):
        new_student = Student03(
            firstname=fake.first_name(), 
            lastname=fake.last_name(), 
            email=fake.email(), 
            group_id=randint(1, count))
        db.session.add(new_student)
    db.session.commit()
    # Добавляем группы
    for group in range(1, count+1):
        new_group = Group03(group=f'group{group}')
        db.session.add(new_group)
    db.session.commit()
    # Добавляем оценки
    for evaluation in range(1, count+1):
        new_evaluation = Evaluation03(
            student_id=randint(1, count),
            evaluation=randint(1, 5),
            lesson_id=randint(1, count))
        db.session.add(new_evaluation)
    db.session.commit()
    # Добавляем занятия
    for lesson in range(1, count+1):
        new_lesson = Lesson03(
            lesson=f'lesson{lesson}')
        db.session.add(new_lesson)
    db.session.commit()
    print('fill_tables it is ok')
    return 'fill_tables it is ok'
    

if __name__ == '__main__':
    app.run(debug=True)