from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

"""FORM CLASS STRUCTURE:

[VARIABLE] = [FIELD TYPE]('[LABEL]', [
        validators=[VALIDATOR TYPE](message=('[ERROR MESSAGE'))
    ])
    
"""

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')