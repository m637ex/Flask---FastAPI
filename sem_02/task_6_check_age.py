# Задание №6
# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы

app = Flask(__name__)


_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/get_age/',
        'name': 'Возраст'},
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


@app.route('/get_age/', methods=['GET', 'POST'])
def len_text():
    context = { # Данный для шаблона
        'title': 'Age',
        'links': _links,
    }
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        print(f'{name = }, {age = }')
        if age > 0 and isinstance(age, int):
            return f'Введено: {name = }, {age = }'
        return f'Возраст {age} введен неверно.'
    return render_template('get_age.html', **context)


if __name__ == '__main__':
    app.run(debug=True)