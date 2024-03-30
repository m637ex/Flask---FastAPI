# Задание №8
# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, 
# где будет выведено "Привет, {имя}!".

# выведено введенное число и его квадрат.


from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы
from flask import redirect # redirect
from flask import url_for # Генерация URL путей
from flask import flash # FLASH сообщения, устанавливаем обязательно app.secret_key

app = Flask(__name__)
app.secret_key = b'8530bb1c858e0a97bba8359867b263d50f9857f57fa4e8b157783fdb0eb69c4d' # flash секрет key


_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/flash_name/',
        'name': 'Ввести Имя'},
]

@app.route('/')
def index():
    context = { # Данные для шаблона
        'title': 'Main',
        'links': _links,
        'image_url': '/static/images/foto.jpg',
    }
    return render_template('index.html', **context)


# FLASH сообщения (не забываем про секретный код)
@app.route('/flash_name/', methods=['GET', 'POST'])
def flash_name():
    context = { # Данный для шаблона
        'title': 'flash_name',
        'links': _links,
    }
    if request.method == 'POST':
        # Проверка данных формы
        user = request.form['name']
        print(f'{user = }')
        if not user:
            flash('Введите имя!', 'danger')
            return redirect(url_for('flash_name'))
        # Обработка данных формы
        flash(f'Привет, {user}', 'success')
        return redirect(url_for('flash_name'))
    return render_template('flash_name.html', **context)

if __name__ == '__main__':
    app.run(debug=True)