from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt   
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY']='2882822821728SAASAS8111'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='Login'
login_manager.login_message_category='info'

from app import routes