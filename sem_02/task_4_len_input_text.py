# Задание №4
# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы
from flask import redirect, url_for

app = Flask(__name__)


_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/len_text/',
        'name': 'Длина тектста'},
]

@app.route('/')
# @app.route('/index/')
def index():
    context = { # Данный для шаблона
        'title': 'Main',
        'links': _links,
        'image_url': '/static/images/image.jpg',
    }
    return render_template('index.html', **context)


@app.route('/len_text/', methods=['GET', 'POST'])
def len_text():
    context = { # Данный для шаблона
        'title': 'Length Text',
        'links': _links,
    }
    if request.method == 'POST':
        text = request.form.get('text')
        print(f'{text = }')
        if not text:
            return redirect(url_for('len_text'))
        return f'Длина текста "{text}" = {len(text)}'
    return render_template('len_text.html', **context)


if __name__ == '__main__':
    app.run(debug=True)


