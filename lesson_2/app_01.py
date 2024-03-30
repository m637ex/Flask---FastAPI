from flask import Flask
from flask import url_for # Генерация URL путей
from flask import render_template # Генерация страниц html
from flask import request # Обработка запросов GET / POST
from flask import abort # Обработка ошибки abort
from flask import redirect # redirect
from flask import flash # FLASH сообщения, устанавливаем обязательно app.secret_key
from flask import make_response # для работы с файлами. Cookie
from flask import session # session, устанавливаем обязательно app.secret_key
from markupsafe import escape
from pathlib import PurePath, Path # для работы с файловой сисетмой
from werkzeug.utils import secure_filename # Безопасность. Переименовывает загружаемые файлы
import logging # включаем логирование
from db import get_blog # импортируем функцию из db.py
app = Flask(__name__)
app.secret_key = b'8530bb1c858e0a97bba8359867b263d50f9857f57fa4e8b157783fdb0eb69c4d' # flash секрет key
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets. token_hex()
"""

logger = logging.getLogger(__name__)


# Cookie settings + сессия
@app.route('/index/')
@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))
    

# make_response
# @app.route('/')
# def index():
#     context = {
#         'title': 'Главная',
#         'name': 'Харитон'
#     }
#     response = make_response(render_template('main.html', **context))
#     response.headers['new_head'] = 'New value'
#     response.set_cookie('username', context['name'])
#     return response

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName' # создаём сессию
        return redirect(url_for('index'))
    return render_template('username_form.html')

@app.route('/logout/')
def logout():
    session.pop('username', None) # закрываем сессию
    return redirect(url_for('index'))


@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"


@app.route('/path/<path:file>/')
def get_file(file):
    print(file)
    # return f'Ваш файл находится в: {file}!' # Позволит злоумышленнику загрузить скрипт вируса
    return f'Ваш файл находится в: {escape(file)}!' # Защитит от скриптов в поле ввода (Пользовательское экранирование)

#========Генерация URL =================
@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>' 
    # => '/test_url_for/42/'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>' 
    # => '/test_url_for/42/?data=new_data'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    # => '/test_url_for/42/?data=new_data&pi=3.14515'
    return text

# внутри =============Генерация пути к статике===============
@app.route('/about/')
def about():
    context = {
    'title': 'Обо мне',
    'name': 'Харитон',
    }
    return render_template('about.html', **context)


# =============Обработка  GET запросов=============
@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'
# http://127.0.0.1:5000/get/?name=alex&age=13&level=80  
# => Похоже ты опытный игрок, раз имеешь уровень 80
#    ImmutableMultiDict([('name', 'alex'), ('age', '13'), ('level', '80')])
# рекомендация использовать  блок try с обработкой KeyError


# ==============Обработка POST запросов=============
@app.route('/submit', methods=['GET', 'POST']) # работает как с GET, так и POST запросами
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'     # ответ на POST запрос
    return render_template('form.html') # Ответ на Get запрос

# Альтернативный метод
@app.get('/submit2')
def submit_get():
    return render_template('form.html')
@app.post('/submit2')
def submit_post():
    name = request.form.get('name')
    return f'Hello {name}!'

# Загрузка файлом через POST запрос
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST': # Получаем пост запрос
        file = request.files.get('file') # Получаем файл 
        file_name = secure_filename(file.filename) # Получаем имя файла и сокращаем его до безопасного методом secure_filename
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name)) # сохранить в текущей директории в католог uploads
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


# функция abort:
@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    # ...
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)
    # ...
    # возвращаем найденную в БД статью

# декоратор для обработки кодов ошибок
@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404 # user увидит страницу 404.html, но код у нее будет 200,т.к. страниуа есть, но в логи пойдет ошибка 404

# Ошибка 500
@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500

# Редирект
@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index')) # переправит на страницу функции def index т.е. "/"

# взять параметр и редирекнуться c /redirect/<name> на /hello/<name> с именем <name>
@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'
@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


# FLASH сообщения (не забываем про секретный код)
@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)