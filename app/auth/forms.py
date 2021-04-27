from .. models import User
from flask_wtf import FlaskForm
from wtforms import PasswordField,SelectField,StringField,SubmitField,BooleanField,ValidationError
from wtforms.validators import EqualTo,Required,Email

class Registration(FlaskForm):
  username = StringField('Enter username',validators=[Required()])
  email=StringField('Enter your Email',validators=[Required(),Email()])
  password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',
  message='passwords must match')])
  password_confirm=PasswordField('confirm passwords',validators=[Required()])
  submit=SubmitField('Sign up')

  def validate_email(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError("This email isalready registered")

  def validate_username(self,data_field):
    if User.query.filter_by(username=data_field.data).first():
      raise ValidationError("username already taken")

class LoginForm(FlaskForm):
  username = StringField("Enter username",validators=[Required()])
  password = PasswordField("Password",validators=[Required()])
  remember=BooleanField("Stay Logged in")
  submit=SubmitField("Login")