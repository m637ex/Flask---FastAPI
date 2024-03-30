# Задание №3
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и 
# переход на страницу приветствия пользователя или страницу с ошибкой.

from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы
from flask import redirect # redirect
from flask import url_for # Генерация URL
# from werkzeug.utils import secure_filename # Безопасность. Переименовывает загружаемые файлы
# import logging # включаем логирование

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': # получим данные из формы
        return f'POST получен'
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST']) 
def hello():
    if request.method == 'POST':
        return f'POST получен' 
    return render_template('login.html')
  
if __name__ == '__main__':
    app.run(debug=True)