from flask import Flask, render_template

app = Flask(__name__)


# Задание №1 Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')   # ○ страницу "about"
def about():
    return render_template('about.html')


@app.route('/contact/')  # ○ страницу "contact".
def contact():
    return render_template('contact.html')


# функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
@app.route('/sum/<int:num1>+<int:num2>/')
def sum(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/len-str/<string:line>')
def len_(line):
    return f'Длина строки: "{line}" составляет {len(line)} символов'

# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

# Решение 1
text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="<KEY>" crossorigin="anonymous">
</head>

# Решение 2
<body>
    <div class="container">
    <div class="jumbotron">
        <h1 class="display-4">Моя первая HTML страница</h1>
        <p> Hello, world! </p>
    </div>
    </div>
</body>
"""

@app.route('/html/')
def html():
    return text

@app.route('/index/')
def index():
    return render_template('index.html')


# Задание №6
# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.
@app.route('/students/')
def students():
    students = [{'name': 'Иван', 'family': 'Иванов', 'age': 20, 'avg': 5},
                {'name': 'Петр', 'family': 'Сидоров', 'age': 21, 'avg': 4},
                {'name': 'Сергей', 'family': 'Петров', 'age': 22, 'avg': 3},
                {'name': 'Александр', 'family': 'Мочалов', 'age': 23, 'avg': 3.5},
                {'name': 'Андрей', 'family': 'Попов', 'age': 24, 'avg': 4.5},
                {'name': 'Вася', 'family': 'Канц', 'age': 25, 'avg': 4.8},
            ]
    context = {'students': students,
               'title': 'Cтраница студентов'}
    return render_template('students.html', **context)

# Задание №8
# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы. 
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.
# базовый шаблон base.html, остальные шаблоны используют его для ганерации

if __name__ == '__main__':
    app.run(debug=True)
