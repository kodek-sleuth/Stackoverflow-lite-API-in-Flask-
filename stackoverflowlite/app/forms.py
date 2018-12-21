from wtforms import Form, PasswordField, StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class  SignUpForm(Form):

    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])

    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=30)])
    
    linkedIn = StringField('LinkedIn', validators=[DataRequired(), Length(max=20)])

    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=100)])
    
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20), EqualTo('confirmpassword', message='Passwords Do not match')])

    confirmpassword = PasswordField('Confirm Password')

    submit = SubmitField( 'CREATE ACCOUNT' )
    
class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('LOGIN ')

class AskQuestion(Form):
    Title = StringField('Title', validators=[DataRequired(), Length(min=10, max=100)])

    Body = TextAreaField('Body', validators=[DataRequired(),Length(min=10,max=400)])

    submit = SubmitField('Ask question')

class AnswerForm(Form):
    Body = TextAreaField('Please Enter your answer in the text-box below', validators=[DataRequired(),Length(min=10,max=400)])
    submit = SubmitField('Add Answer')

class  UpdateForm(Form):

    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])

    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=30)])
    
    linkedIn = StringField('LinkedIn', validators=[DataRequired(), Length(max=20)])

    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=100)])
    
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=15)])

    picture = FileField('Please choose a Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    
    submit = SubmitField( 'Update' )

class StackmailForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=100)])

    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Enter StackMail')




