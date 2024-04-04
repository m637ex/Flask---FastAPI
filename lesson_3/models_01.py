from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model): # модель для создания таблицы дочеркий класс db
    id = db.Column(db.Integer, primary_key=True) # integer - числа int, primary - главное поле() само проставляется
    username = db.Column(db.String(80), unique=True, nullable=False) # колонка string- строковая, 80 - макс длина поля
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # db.Integer - целые числа
    # primary_key=True - главный ключ, автопростановка с 1 +1
    # unique=True - уникальное поле
    # nullable=False - поле НЕ может быть пустым
    # default=datetime.utcnow - дефолтное значение поля - текущее время
    posts = db.relationship('Post', backref='author', lazy=True) # Посты пользователя, связь с class Post()
    # db.relationship - взаимодействие с "Post"
    # backref='author' - обратная ссылка 
    # Lazy=True - ленивый режим, формируем связи только когда нужно.

    def __repr__(self): # информация для вывода
        return f'User({self.username}, {self.email})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # связка class User / id
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # db.ForeignKey('user.id') - Автор ID из другой таблицы

    def __repr__(self):
        return f'Post({self.title}, {self.content})'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) # Комментарий привязываем к статье
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # привязываем автора комментария
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'Comment({self.content})'