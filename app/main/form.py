from wtforms import Form, PasswordField, StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError


class StackmailForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=100)])

    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Enter StackMail')