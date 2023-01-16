from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_qrcode import QRcode


# Set app


db = SQLAlchemy()


def create_app():
    """
    Config & create app
    """
    app = Flask(__name__)
    QRcode(app)

    app.config['SECRET_KEY'] = 'fvdfvfdmjmkmklwjjnjfwef'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register models 
    
    from .models import User

    with app.app_context():
        db.create_all()

    # Authentication setup

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app

