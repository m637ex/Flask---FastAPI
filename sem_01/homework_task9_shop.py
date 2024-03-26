# Задание №9
# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

    """
    Используем файл шаблона:
    shop_base.html
    
    и страницы шаблона: 
    shop_cloth.html 
    shop_shoes.html 
    shop_jacket.html    
    """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/shop_cloth/')
def index():
    return render_template('shop_cloth.html')


@app.route('/shop_shoes/')
def shop_shoes():
    return render_template('shop_shoes.html')


@app.route('/shop_jacket/')
def shop_jacket():
    return render_template('shop_jacket.html')

@app.route('/<string:line>/') # Возвращает на туже страницу. Относительная ссылка
def len_(line):
    return '<p><a href="../">Страница не доступна, нажмите чтобы вернуться обратно</a></p>'


if __name__ == '__main__':
    app.run(debug=True)