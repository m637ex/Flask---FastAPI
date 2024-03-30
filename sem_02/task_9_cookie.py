# Задание №9
# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.




from flask import Flask
from flask import render_template # генерация шаблона
from flask import request # GET POST  запросы
from flask import redirect # redirect
from flask import url_for # Генерация URL путей
from flask import flash # FLASH сообщения, устанавливаем обязательно app.secret_key
from flask import session
from flask import make_response

app = Flask(__name__)
app.secret_key = b'8530bb1c858e0a97bba8359867b263d50f9857f57fa4e8b157783fdb0eb69c4d' # flash секрет key


_links = [ # список ссылок для меню
    {'url': '/',
        'name': 'Главная'},
    {'url': '/login/',
        'name': 'Вход'},
    {'url': '/logout/',
        'name': 'Выход'},
]


@app.route('/')
@app.route('/index/')
def index():
    context = { # Данные для шаблона
        'title': 'Main',
        'links': _links,
        'image_url': '/static/images/foto.jpg',
        'name': 'Anonimus'
    }    
    if 'username' in session:
        context['name'] = request.cookies.get('username')
    return render_template('index.html', **context)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = { # Данный для шаблона
        'title': 'login',
        'links': _links,
        'image_url': '/static/images/foto.jpg',
        'name': request.form.get('login'),
    }    
    if request.method == 'POST': # получим данные из формы        
        # Проверка данных формы
        session['username'] = request.form.get('username') or 'Anonimus' # создаём сессию
        login = request.form.get('login')
        email = request.form.get('email')
        password = request.form.get('password')
        response = make_response(redirect(url_for('index')))  
        response.set_cookie('username', login)  
        if not login:
            flash('Введите имя!', 'danger')
            return redirect(url_for('login'))       
        elif not email:
            flash('Введите email!', 'danger')
            return redirect(url_for('login'))     
        elif not password:
            flash('Введите email!', 'danger')
            return redirect(url_for('login'))
        flash(f'С возвращением, {login}', 'success')
        return response # redirect(url_for('index'))        
    return render_template('login.html', **context)


@app.route('/logout/')
def logout():
    session.pop('username', None) # закрываем сессию
    flash(f'Вы вышли из сесиии успешно', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
    
    