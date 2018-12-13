from flask import Flask,render_template,url_for,flash,redirect,request,session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import SignUpForm, LoginForm, AskQuestion
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='2882822821728SAASAS8111'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(13), nullable=False)
    lastname = db.Column(db.String(13), nullable=False)
    country = db.Column(db.String(60), nullable=False)
    linkedIn = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    image_file = db.Column(db.String(60), default='default.jpg', nullable=False)

    def __init__(self,firstname,lastname,country,linkedIn,email,username,password):
        self.firstname=firstname
        self.lastname=lastname
        self.country=country
        self.linkedIn=linkedIn
        self.email=email
        self.username=username
        self.password=password
    
    def __repr__(self):
        return '<username {}'.format(self.username)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(13), nullable=False)
    lastname = db.Column(db.String(13), nullable=False)
    country  = db.Column(db.String(60), nullable=False)
    linkedIn = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    image_file = db.Column(db.String(60), default='default.jpg', nullable=False)
    question = db.relationship('Questions', backref='Author', lazy=True)
    
    def __init__(self,firstname,lastname,country,linkedIn,email,username,password):
        self.firstname=firstname
        self.lastname=lastname
        self.country=country
        self.linkedIn=linkedIn
        self.email=email
        self.username=username
        self.password=password
    
    def __repr__(self):
        return '{}-{}'.format(self.username,self.email)

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.String(300), nullable=False)
    Date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __init__(self,Title,Content,User_id):
        self.Title=Title
        self.Content=Content
        self.User_id=User_id

    def __repr__(self):
        return '{}-{}'.format(self.Title,self.Date_posted)

@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/SignUp", methods=['GET','POST'])
def SignUp():
    form = SignUpForm(request.form)

    if form.validate():
        hashed_pw=bcrypt.generate_password_hash(form.password.data)
        db.create_all()

        try:
            user=User(firstname=form.firstname.data, lastname=form.lastname.data, country=form.country.data, linkedIn=form.linkedIn.data, email=form.email.data, username=form.username.data, password=hashed_pw)
            user1=User.query.filter_by(username=form.username.data).first()
            user2=User.query.filter_by(email=form.email.data).first()
            
            if user1:
                flash("Username already taken","danger")

            elif user2:
                flash("Email already taken","danger")
            
            else:
                db.session.add(user)
                db.session.commit()
                flash("{} you have successfully Created Your account, Login Kindly".format(form.username.data), "success")
                return redirect(url_for("Login"))
        except:
            flash("Account  already has A user by that exact description","danger")
    
    return render_template("signup.html", form=form)

@app.route("/Login", methods=['GET','POST'])
def Login():
    form = LoginForm(request.form)

    if form.validate():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                return redirect(url_for("Home"))
            else:
                flash("Invalid Password or Username, Try Again","danger")
                return redirect(url_for("Login"))   
        except:
             flash("Invalid Credentials, Please either register or Retry with Correct Credentials","danger")
    return render_template("login.html", form=form)

@app.route("/Users")
def Users():
    return render_template("Users.html")

@app.route("/Profile")
def Profile():
    return render_template("profile.html")

@app.route("/askquestion", methods=['GET','POST'])
def askquestion():
    form = AskQuestion(request.form)
    if form.validate():
        return redirect(url_for('Home'))
    return render_template("askquestion.html",form=form)

@app.route("/Home")
def Home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)



