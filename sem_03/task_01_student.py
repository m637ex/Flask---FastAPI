# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.


from flask import Flask
from sem_03.models_01_student import db, Student, Gender, Faculty, Group
from random import randint
# pip install faker
from flask import render_template
from faker import Faker # Faker - это библиотека для генерации случайных данных на различных языках программирования
fake = Faker()

app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar-flask-db.db'   # Задаём тип и место БД
db.init_app(app)

@app.route('/') 
def index():     
    return 'Hi!'

@app.route('/students/') 
def all_students():  
    students = Student.query.all() #обращение к модели  Student, с запросом query на all - всё
    context = {'students': students} # словарь контекста
    return render_template('students.html', **context)


@app.route('/init-db/') 
# @app.cli.command("init-db")  # запуск из командной строки через  flask init-db (нужно изменить пути импорта библиотек!!!)
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all() # создай таблицы в БД
    print ("init-db 0K")
    return "init-db 0K"


@app.route('/fill-db/') 
# @app.cli.command("fill-db") # ➢Наполнение тестовыми данными (нужно изменить пути импорта библиотек!!!)
def fill_tables():
    count = 12
    count_group = 10
    count_faculty = 4
    # Добавляем Студентов
    for student in range(1, count + 1):
        new_student = Student(
            firstname=fake.first_name(), 
            lastname=fake.last_name(), 
            age=fake.random_int(min=18, max=30), 
            gender_id=randint(1, 2), 
            group_id=randint(1, count_group), 
            faculty_id=randint(1, count_faculty))
        db.session.add(new_student)
    db.session.commit()
    # Добавляем факультеты
    for faculty in range(1, count_faculty+1):
        new_faculty = Faculty(faculty=f'faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    # Добавляем группы
    for group in range(1, count_group+1):
        new_group = Group(group=f'group{group}')
        db.session.add(new_group)
    db.session.commit()
    # Добавляем пол
    men = Gender(gender='men')
    db.session.add(men)
    women = Gender(gender='women')
    db.session.add(women)
    db.session.commit()
    print('fill_tables it is ok')
    return 'fill_tables it is ok'
    

if __name__ == '__main__':
    app.run(debug=True)