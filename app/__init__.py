from app import *
from app.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt   
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view='User.Login'
login_manager.login_message_category='info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.AskQuestion.routes import AskQuestion_blueprint
    from app.main.routes import main_blueprint
    from app.Single_Question.routes import Single_Question_blueprint
    from app.User.routes import User_blueprint
    from app.Users.routes import Users_blueprint

    app.register_blueprint(AskQuestion_blueprint)
    app.register_blueprint(Single_Question_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(User_blueprint)
    app.register_blueprint(Users_blueprint)

    return app


