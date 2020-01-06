from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Создать экзенмпляр приложения Flask
app = Flask(__name__)
# Задать конфигурацию приложения из импортированного класса
app.config.from_object(Config)
# Создать коннектор базы данных
db = SQLAlchemy(app)
# Создать объект миграции базы данных
migrate = Migrate(app, db)
# Создать объект login менеджера пользовательской сессии
login = LoginManager(app)
# Объявить имя функции логина для поиска с помощью url_for
login.login_view = 'login'


from app import routes, models
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    """ Импортировать по умолчанию объекты для работы из консоли """
    return {'db': db, 'User': User, 'Post': Post}

