# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при нажатии на которую будет переход на
# другую страницу с приветствием пользователя по имени.


from flask import Flask
from flask import request  # Обработка запросов GET / POST
from flask import render_template  # Генерация страниц html

app = Flask(__name__)


@app.get('/') 
def index_get():
    return render_template('form.html')
    # переход по '/' вызывает запрос GET и открывает форму  form.html
    # делее при нажатии книпки в форме вызывается запрос post и работает функция index_post()

@app.post('/')
def index_post():
    name = request.form.get('name') # получаем name из form.html
    return f'Привет, {name}'


if __name__ == '__main__':
    app.run(debug=True)
