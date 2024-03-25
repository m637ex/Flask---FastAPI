from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/Николай/') # путь в адресной строке браузера
def nike():
    return 'Привет, Николай! '


@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'


@app.route('/Фёдор/')   # Множественное декорирование
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'


@app.route('/')
@app.route('/<name>/')  # <> для использования переменной "name" в стоке адреса
def hello(name='незнакомец'):  # name='незнакомец' - значение по умолчанию
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>/')  # Указатель на путь /file/<path:file>/
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'


# указатель на вещественное число (/number/42.0)
@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


# ===========ВЫВОД HTML ФАЙЛА=============
html = """
<p>Вот не думал, не гадал,<br>Программистом взял и
стал.<br>Хитрый знает он язык,<br>Он к другому не привык.</p>
"""


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    # формируем список poem в строку с разделителем <br/> (перенос строки)
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt


# ===========Рендеринг HTML файла с использованием Jinja2=============
@app.route('/index/')
def index():
    context = {     # Словарь данных
    'title': 'Личный блог',
    'name': 'Андрей Омельчук',
    'user': 'Крутой Хакер!',
    'number': 1,
    }
    return render_template('index1.html', **context) # index - шаблон, **context - словарь данных

#==========Ветвление==========
@app.route('/if/')  # Отработка условия if
def show_if(): 
    context = {'title': 'Ветвление', 
               'user': 'Крутой xaкep!', 
               'number': 1, 
               }
    return render_template('show_if.html', **context)

#===========Цикл==============
@app.route('/for/')
def show_for():
    context =   {
            'title': 'Ветвление',
            'poem': ['Вот не думал, не гадал,',
                    'Программистом взял и стал.',
                    'Хитрый знает он язык,',
                    'Он к другому не привык.',
                    ]
            }
    # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>'.join(poem) + '</p>'
    return render_template('show_for.html', **context)

# ===========Сложная структра в цикле============
@app.route('/users/')
def users():
    _users = [{ 'name': 'Никанор',
                'mail': 'nik@mail.ru',
                'phone': '+7-987-654-32-10',
                },
                {'name': 'Феофан',
                'mail': 'feo@mail.ru',
                'phone': '+7-987-444-33-22',
                },
                {'name': 'Оверран',
                'mail': 'forest@mail.ru',
                'phone': '+7-903-333-33-33',
                }, ]
    context = {'users': _users,
               'title': 'Точечная нотация' }
    return render_template('users.html', **context)

# =============Наследование шаблонов===============
# ------Базовый сценарий--------- # 2 файла с однотипным содержимым
@app.route('/main/') 
def main(): 
    context = {'title': 'Главная' } 
    return render_template('main.html', **context)
@app.route('/data/') 
def data(): 
    context = {'title': 'basa статей' } 
    return render_template('data.html', **context)

#------------Наследование-------------
# 3 файла но один шаблон с общей информацие и 2 файна с небольшим количетсвом уникальной информацией для шаблона
@app.route('/newmain/') 
def main(): 
    context = {'title': 'Главная' } 
    return render_template('new_main.html', **context)
@app.route('/newdata/') 
def data(): 
    context = {'title': 'База статей' } 
    return render_template('new_data.html', **context)


if __name__ == '__main__':
    app.run()


# C лекции идет ссылка в коде на bootstrap.min.css при этом никак не сказано как она установилась в python, но судя по коду непонятно как она сутановилась в папку программы