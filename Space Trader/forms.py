from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange


class Value(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = "Number of skill points can't be negative"
        self.message = message

    def __call__(self, form, field):
        sp = field.data
        if sp < 0:
            raise ValidationError(self.message)


value = Value(0, 16)


class SettingForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    diff = SelectField(
        "Difficulty", choices=[("easy", "Easy"), ("med", "Medium"), ("hard", "Hard")]
    )
    submit = SubmitField("Continue")


class SPForm(FlaskForm):

    # spLimit = 0
    # def __init__(self, spLimit, *args, **kwargs):
    #   super(SPForm, self).__init__(*args, **kwargs)
    #   self.spLimit = spLimit

    sp1 = IntegerField("SP1", validators=[DataRequired(), NumberRange(min=0)])
    sp2 = IntegerField("SP2", validators=[DataRequired(), NumberRange(min=0)])
    sp3 = IntegerField("SP3", validators=[DataRequired(), NumberRange(min=0)])
    sp4 = IntegerField("SP4", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Continue")

    # def validate(self):
    #   if not super(SPForm, self).validate():
    #        return False
    #    if (self.sp1.data + self.sp2.data + self.sp3.data + self.sp4.data) <= self.spLimit:
    #        return True
    #    self.sp1.errors.append("Total skillpoints cannot be over " +spLimit+".")
    #    return False


class ConfirmForm(FlaskForm):
    submit = SubmitField("Confirm")
