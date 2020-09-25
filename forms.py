from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField

class CreateEntryForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    timeSpent = IntegerField('timeSpent', validators=[DataRequired(message="must enter a number for this field")])
    learned = TextAreaField('learned', validators=[DataRequired()])
    resources = TextAreaField('resources', validators=[DataRequired()])
    date = DateTimeLocalField('date', validators=[DataRequired()], format='%Y-%m-%d')
