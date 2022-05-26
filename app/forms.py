from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('subject', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('content', validators=[
        DataRequired('The content is required')
    ])

class UserCreateForm(FlaskForm):
    username = StringField('User name', validators=[
        DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('password', validators=[
        DataRequired(), EqualTo('password2', 'passowrd is discorrect')])
    password2 = PasswordField('Check the passowrd', validators=[DataRequired()])
    email= EmailField('email', [DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username=StringField('username', validators=[
        DataRequired(), Length(min=3, max=25)])
    password = PasswordField('password', validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])

class UserSearchPw(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(), Length(min=3, max=25)])
    email= EmailField('email', [DataRequired(), Email()])

class UserAuthenticPw(FlaskForm):
    pin = StringField('pin', validators=[
        DataRequired()])

class AddressForm(FlaskForm):
    address = TextAreaField('주소', validators=[DataRequired()])