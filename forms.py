from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class PlayerForm(FlaskForm):
    bat_order = IntegerField('Bat Order', validators=[DataRequired(), NumberRange(min=1)])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    at_bats = IntegerField('At Bats', validators=[NumberRange(min=0)])
    hits = IntegerField('Hits', validators=[NumberRange(min=0)])