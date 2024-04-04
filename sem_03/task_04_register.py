# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.



from flask import Flask, render_template, request 
from flask_wtf.csrf import CSRFProtect
from form_04 import LoginForm, RegistrationForm

app = Flask(__name__) 
app.config[ 'SECRET_KEY'] = b'8530bb1c858e0a97bba8359867b263d50f9857f57fa4e8b157783fdb0eb69c4d'
csrf = CSRFProtect(app)

@app.route('/') 
def index(): 
    return 'Н1!'


@app.route('/login/', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if request.method == 'POST' and form.validate(): # проверка что вернулся post запрос и форма прошла валидацию
        # Обработка данных из формы 
        return 'Access!!!'
        pass        
    return render_template('Login.html', form=form) 
    

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data
        email = form.email.data
        password = form.password.data
        birthday = form.birthday.data
        print(name, email, password, birthday)
    return render_template('register.html', form=form)


if __name__ == '__main__': 
    app.run(debug=True)