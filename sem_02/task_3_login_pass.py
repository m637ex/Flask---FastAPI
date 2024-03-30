# Задание №3
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и 
# переход на страницу приветствия пользователя или страницу с ошибкой.

from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы
from flask import abort # вызов ошибки

app = Flask(__name__)

users = {'Andrey': '123456', 'John': '456789'}
_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/login/',
        'name': 'Вход'},
    # {'url': '/logout/',
    #  'name': 'Выход'}
]

@app.route('/')
# @app.route('/index/')
def index():
    context = { # Данный для шаблона
        'title': 'Image',
        'links': _links,
        'image_url': '/static/images/image.jpg',
    }
    return render_template('index.html', **context)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = { # Данный для шаблона
        'title': 'login',
        'links': _links,
        'name': request.form.get('login'),
    }    
    if request.method == 'POST': # получим данные из формы
        login = request.form.get('login')
        password = request.form.get('password')
        if login in users.keys() and users[login] == password:
            return render_template('index.html', **context)
        else:
            abort(403)
    return render_template('login.html', **context)
        

@app.route('/403/')
@app.errorhandler(403)
def access_is_denied(e):
    # app.logger.warning(e)
    context = {
        'title': 'Доступ запрещён',
    }
    return render_template('403.html', **context), 403 # в логи пойдет ошибка 403, в браузер 200

        
if __name__ == '__main__':
    app.run(debug=True)