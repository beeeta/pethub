from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class RegisterForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    rept_password = StringField('rept_password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

