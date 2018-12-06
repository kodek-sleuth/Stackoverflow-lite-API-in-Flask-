from wtforms import Form, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class  SignUpForm(Form):

    first_name = StringField('First Name', validators=[DataRequired(), Length(min=4, max=12)])
    
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=4, max=12)])

    country = StringField('Country', validators=[DataRequired(), Length(min=2, max=30)])
    
    linkedIn = StringField('LinkedIn', validators=[DataRequired(), Length(max=20)])

    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=8, max=100)])
    
    username = StringField('Username', validators=[DataRequired(), Length(min=7, max=12)])
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20), EqualTo('comfirm_password', message='Passwords Do not match')])

    confirm_password = PasswordField('Confirm Password')

    submit = SubmitField( 'CREATE ACCOUNT' )

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=7, max=20)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])

    submit = SubmitField('LOGIN ')