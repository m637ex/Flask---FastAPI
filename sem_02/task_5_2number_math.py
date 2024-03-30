# Задание №5
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции 
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции 
# и переход на страницу с результатом.

from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы
from flask import redirect, url_for

app = Flask(__name__)


_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/math/',
        'name': 'Математика'},
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


@app.route('/math/', methods=['GET', 'POST'])
def len_text():
    context = { # Данный для шаблона
        'title': 'Math',
        'links': _links,
    }
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        act = request.form.get('act')
        num2 = int(request.form.get('num2'))
        print(f'{num1 = }, {act = }, {num2 = }')
        match act:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                result = num1 / num2
            case _:
                result = None
        if not num1 and not num2:
            return redirect(url_for('math'))
        return f'Введено: {num1} {act} {num2} = {result}'
    return render_template('math.html', **context)


if __name__ == '__main__':
    app.run(debug=True)