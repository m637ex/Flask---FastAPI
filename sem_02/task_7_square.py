# Задание №7
# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы

app = Flask(__name__)


_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/square/',
        'name': 'Квадрат числа'},
]

@app.route('/')
def index():
    context = { # Данные для шаблона
        'title': 'Main',
        'links': _links,
        'image_url': '/static/images/foto.jpg',
    }
    return render_template('index.html', **context)



@app.route('/square/', methods=['GET', 'POST'])
def len_text():
    context = { # Данный для шаблона
        'title': 'Square',
        'links': _links,
    }
    if request.method == 'POST':
        num = int(request.form.get('num'))
        print(f'{num = }')
        return f'Квадрат числа {num}, будет равен {num * num}'
    return render_template('square.html', **context)


if __name__ == '__main__':
    app.run(debug=True)