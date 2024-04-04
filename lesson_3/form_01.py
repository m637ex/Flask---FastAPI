from flask import Flask
from flask_wtf import FlaskForm # обеспечивает валидацию форм
from wtforms import StringField, PasswordField, IntegerField, SelectField # прверки полей формы
from wtforms.validators import DataRequired, Email, EqualTo, Length # Валидация данных формы

from flask_wtf.csrf import CSRFProtect  # защиты от CSRF-атак

app = Flask(__name__)
app.config['SECRET_KEY'] = b'8530bb1c858e0a97bba8359867b263d50f9857f57fa4e8b157783fdb0eb69c4d'
csrf = CSRFProtect(app) # получаем csrf для работы с формами


@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt # этим ключём можно отправить незащищенную форму пользователю
def my_form():
    return 'No CSRF protection!' 


class LoginForm(FlaskForm): # каждый класс форм наследуется  от класса FlaskForm
    username = StringField('Username', validators=[DataRequired()]) # описываем поля
    password = PasswordField('Password', validators=[DataRequired()])
    # валидация validators=[DataRequired()] - данные требуются, можно использовать несколько проверок 

# WTForms предоставляет множество типов полей для формы. Вот некоторые из них:
# ● StringField — строковое поле для ввода текста;
# ● IntegerField — числовое поле для ввода целочисленных значений;
# ● FloatField — числовое поле для ввода дробных значений;
# ● BooleanField — чекбокс;
# ● SelectField — выпадающий список;
# ● DateField — поле для ввода даты;
# ● FileField — поле для загрузки файла.
# ● ...

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Мужчина'), ('female', 'Женщина')]) # выбор полей формы из списка


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) # строковое поле, email
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)]) # поле арроль  длиной мин 6 символов
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) # EqualTo - как passwords выше



if __name__ == '__main__': 
    app.run(debug=True)
    