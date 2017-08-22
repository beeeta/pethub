from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AddPetForm(Form):
    kind = StringField('username', validators=[DataRequired()])
    city = StringField('password', validators=[DataRequired()])
    link = StringField('email', validators=[DataRequired()])


