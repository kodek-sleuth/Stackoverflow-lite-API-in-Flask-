from wtforms import Form, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class AnswerForm(Form):
    Body = TextAreaField('Please Enter your answer in the text-box below', validators=[DataRequired(),Length(min=10,max=400)])
    submit = SubmitField('Add Answer')
