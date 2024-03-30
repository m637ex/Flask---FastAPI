# Задание №2
# Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет
# отображаться форма для загрузки изображений.

from pathlib import Path, PurePath
from flask import Flask
from flask import render_template
from flask import request # запросы GET и POST
from werkzeug.utils import secure_filename # Безопасность. Переименовывает загружаемые файлы

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def image():
    _links = [ # список ссылок для меню
        {'url': '/',
         'name': 'Главная'},
        {'url': '/uploads/',
         'name': 'Загрузить изображение'},
    ]
    context = { # Данный для шаблона
        'title': 'Image',
        'links': _links,
        # 'name': 'Андреандр',
        'image_url': '/static/images/image.jpg',
    }
    return render_template('index.html', **context)


@app.route('/uploads/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file_name = secure_filename(file. filename)
            save_directory = Path.cwd() / 'uploads'
            save_directory.mkdir(parents=True, exist_ok=True) # создать родительскую папку
            file.save(save_directory / file_name)
            save_path = PurePath.joinpath(Path.cwd(), 'uploads', file_name)
            print("Путь сохранения файла:", save_path)
            return f"Файл {file_name} загружен на сервер"
    return render_template('uploads.html')


if __name__ == '__main__':
    app.run(debug=True)