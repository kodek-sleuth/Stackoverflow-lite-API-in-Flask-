from datetime import datetime
from app import db, login_manager, UserMixin

@login_manager.user_loader
def load_user(User_id):
    return User.query.get(int(User_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(13), nullable=False)
    lastname = db.Column(db.String(13), nullable=False)
    country = db.Column(db.String(60), nullable=False)
    linkedIn = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    image_file = db.Column(db.String(1000), default='default.jpg', nullable=False)

    def __init__(self,firstname,lastname,country,linkedIn,email,username,password):
        self.firstname=firstname
        self.lastname=lastname
        self.country=country
        self.linkedIn=linkedIn
        self.email=email
        self.username=username
        self.password=password
    
    def __repr__(self):
        return '{}'.format(self.username)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(13), nullable=False)
    lastname = db.Column(db.String(13), nullable=False)
    country  = db.Column(db.String(60), nullable=False)
    linkedIn = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    image_file = db.Column(db.String(10000), default='default.jpg', nullable=False)
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
        return '{}'.format(self.username)

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Content = db.Column(db.String(300), nullable=False)
    Date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    answers = db.relationship('Answers', backref='AnswerAuthor', lazy=True)
    
    def __init__(self,Title,Content,User_id):
        self.Title=Title
        self.Content=Content
        self.User_id=User_id

    def __repr__(self):
        return '{}'.format(self.Title)

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Body = db.Column(db.String(300), nullable=False)
    Question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    Date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self,Body,Question_id):
        self.Body=Body
        self.Question_id=Question_id

    def __repr__(self):
        return '{}'.format(self.Body)