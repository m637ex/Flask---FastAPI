# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и 
# id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы". Написать функцию-обработчик, которая 
# будет выводить список всех книг с указанием их авторов.

from flask import Flask
from sem_03.models_02_books import db, Book, Author
from random import randint
from flask import render_template 
# pip install faker
from faker import Faker # Faker - это библиотека для генерации случайных данных на различных языках программирования
fake = Faker()

app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar-flask-db.db'   # Задаём тип и место БД
db.init_app(app)


@app.route('/') 
def index():     
    return 'Hi!'

@app.route('/books/') 
def all_books():  
    books = Book.query.all() #обращение к модели  Book, с запросом query на all - всё
    context = {'books': books} # словарь контекста
    print(f'{books = }')
    return render_template('books.html', **context)


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
    # Добавляем книги
    for book in range(1, count + 1):
        new_book = Book(
            title=fake.sentence(), 
            publish_year=fake.random_int(min=1900, max=2024), 
            publish_count=randint(1, 100000), 
            author_id=randint(1, count))
        db.session.add(new_book)
    db.session.commit()
    # Добавляем авторов
    for author in range(1, count + 1):
        new_author = Author(
            firstname=fake.first_name(), 
            lastname=fake.last_name(), )
        db.session.add(new_author)
    db.session.commit()
    print('fill_tables it is ok')
    return 'fill_tables it is ok'
    

if __name__ == '__main__':
    app.run(debug=True)