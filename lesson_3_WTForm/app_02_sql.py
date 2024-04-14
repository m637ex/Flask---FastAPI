from flask import Flask 
from flask import render_template # отрисовка шаблонов
from flask import jsonify # функция возвращает json объект
# from lesson_3.models_01 import db, User, Post, Comment # импортирыем все ранее созданные модели
from models_01 import db, User, Post, Comment # импортирыем все ранее созданные модели
from datetime import datetime, timedelta

app = Flask(__name__) 
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'   # Задаём тип и место БД
db.init_app(app)


@app.route('/') 
def index():     
    return 'Hi!'


@app.cli.command("init-db")  # запуск из командной строки через  flask init-db
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all() # создай таблицы в БД
    print ("0K")
    

@app.cli.command("add-john")  # запуск из командной строки через flask add-john
def add_user():
    user = User(username='john', email='john@example.com') # созлаём экземпляр класса User
    db.session.add(user)    # открываем сессию с БД с данными класса User. Предзагрузка в БД
    db.session.commit()     # фикстрыем изменения и сохраненние в базе
    print('John add in DB!')

    
@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first() # созлаём экземпляр класса User
    # к таблице 'USER' хотим сделать 'query' - объект запрос c фильтром 'filter_by' c username='john' до .first() - первого найденного 
    user.email = 'new_email@example.com' # меняем почту у объекта user
    db.session.commit() # фиксируем изменения
    print('Edit John mail in DB!')


@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first() # созлаём экземпляр класса User
    db.session.delete(user) # Удаляем данные
    db.session.commit() # фиксируем изменения
    print('Delete John from DB!')


@app.cli.command("fill-db") # ➢Наполнение тестовыми данными
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()


@app.route('/data/')
def data():
    return 'Your дата! '


@app.route('/users/')
def all_users():
    users = User.query.all() #обращение к модели пользователя User, с запросом query на all - всё
    context = {'users': users} # словарь контекста
    return render_template('users.html', **context)

# Фильтрация данных 
@app.route('/users/<username>/') # вывести данные по <username>
def users_by_username(username):
    users = User.query.filter(User.username == username).all() # зарос query с фильтром -
    # "User.username == username",  у которых свойство (username) равно значению username
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/') # вывести данные по <user_id>
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(         # Возвращает json объект
            [{'id': post.id, 
              'title': post.title, 
              'content': post.content, 
              'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404 # Возвращает json объект и ошибку 404


# фильтр посто за последнюю неделю
@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7) # дата начала поиска
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([        # Возвращает json объект
            {'id': post.id, 
             'title': post.title,
             'content': post.content, 
             'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404       # Возвращает json объект


if __name__ == '__main__': 
    app.run(debug=True)
    
