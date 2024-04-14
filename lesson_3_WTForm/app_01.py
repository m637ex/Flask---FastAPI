from flask import Flask
from lesson_3.models_01 import db # импортируем db из файла настроек


app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username: password@hostname/db_name'
# app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/db_name'
db.init_app(app) # Строка инициализации БД


@app.route('/') 
def index(): 
    return 'Hi!'


if __name__ == '__main__': 
    app.run(debug=True)