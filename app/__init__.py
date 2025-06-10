from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import time

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Конфигурация подключения к PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:postgres@db:5432/flask_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Инициализация расширений
    db.init_app(app)

    def wait_for_db():
        while True:
            try:
                with app.app_context():
                    db.create_all() 
                break
            except Exception as e:
                print(f"Database not ready yet: {e}")
                time.sleep(5)

    wait_for_db() 
    # Импорт и регистрация маршрутов
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    

    return app
