from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class Value(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = 'Number of skill points can\'t be negative'
        self.message = message

    def __call__(self, form, field):
        sp = field.data
        if sp < 0:
            raise ValidationError(self.message)

value = Value(0, 16)

class SettingForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    diff = SelectField('Difficulty', choices = [('easy', 'Easy'), ('med', 'Medium'), ('hard', 'Hard')])
    sp1 = IntegerField('SP1', validators=[DataRequired(), value])
    sp2 = IntegerField('SP2', validators=[DataRequired(), value])
    sp3 = IntegerField('SP3', validators=[DataRequired(), value])
    sp4 = IntegerField('SP4', validators=[DataRequired(), value])
    submit = SubmitField('Continue')

class ConfirmForm(FlaskForm):
    submit = SubmitField("Confirm")
