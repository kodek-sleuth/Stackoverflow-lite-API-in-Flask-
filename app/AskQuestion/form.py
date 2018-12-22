from wtforms import Form, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class AskQuestionForm(Form):
    Title = StringField('Title', validators=[DataRequired(), Length(min=10, max=100)])

    Body = TextAreaField('Body', validators=[DataRequired(),Length(min=10,max=400)])

    submit = SubmitField('Ask question')