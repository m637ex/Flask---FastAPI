"""
Защитный файл сервера
"""

from lesson_1.app_01 import app

if __name__ == "__main__":
    app.run(debug=True) # debug Сервер в режиме отладки