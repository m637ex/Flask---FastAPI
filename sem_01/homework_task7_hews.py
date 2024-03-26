# Задание №7
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/news/')
def index():
    posts = [{'title': 'ЕЭК освободила от пошлин отдельные виды товаров для производства трансформаторов',
                 'news': 'Совет Евразийской экономической комиссии принял решение предоставить тарифную льготу в виде освобождения от уплаты ввозной таможенной пошлины в отношении отдельных видов товаров для производства электротехнической продукции.', 
                 'date': '2024-03-26 18:00'},
                {'title': 'Кипр и США подпишут соглашение о сотрудничестве в борьбе с отмыванием денег',
                 'news': 'Правительства Соединенных Штатов и Кипра объявили о намерении усилить свое сотрудничество для укрепления возможностей европейской страны в противодействии и преследовании незаконных финансовых операций. Об этом сообщает Reuters.', 
                 'date': '2024-03-26 17:46'},
                {'title': 'Страны Балтии и Чехия предлагают ЕС запретить импорт черных металлов из РФ',
                 'news': 'Страны Балтии, а также Чехия предложили ЕС запретить импорт черных металлов, медных и алюминиевых отходов и лома из России. Об этом сообщает LRT.', 
                 'date': '2024-03-26 17:20'},
                {'title': 'Беларусь прорабатывает с Росатомом строительство мобильного атомного реактора',
                 'news': 'Беларусь прорабатывает с Росатомом проект по строительству мобильного атомного реактора. Об этом заявил академик - секретарь отделения физико-технических наук Национальной академии наук Беларуси Сергей Щербаков в рамках международного форума "Атомэкспо" в Сочи.', 
                 'date': '2024-03-26 17:05'},
            ]
    context = {'posts': posts,
               'title': 'Cтраница новостей'}
    return render_template('news.html', **context)

@app.route('/<string:line>/') # Возвращает на туже страницу. Относительная ссылка
def len_(line):
    return '<p><a href="../news/">Страница не доступна, нажмите чтобы вернуться обратно</a></p>'


if __name__ == '__main__':
    app.run(debug=True)