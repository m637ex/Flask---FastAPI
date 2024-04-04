from flask import Flask, render_template, request 
from flask_wtf.csrf import CSRFProtect

from form_01 import LoginForm, RegistrationForm

app = Flask(__name__) 
app.config[ 'SECRET_KEY'] = b'8530bb1c858e0a97bba8359867b263d50f9857f57fa4e8b157783fdb0eb69c4d'
csrf = CSRFProtect(app)

@app.route('/') 
def index(): 
    return 'Н1!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/login/', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if request.method == 'POST' and form.validate(): # проверка что вернулся post запрос и форма прошла валидацию
        # Обработка данных из формы 
        pass        
    return render_template('Login.html', form=form) 
    

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)


if __name__ == '__main__': 
    app.run(debug=True)