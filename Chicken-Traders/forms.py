from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange


class SettingForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    diff = RadioField(
        "Difficulty",
        choices=[("easy", "Easy"), ("med", "Medium"), ("hard", "Hard"), ],
        default="easy"
    )
    submit = SubmitField("Continue")


class SPForm(FlaskForm):

    sp_limit = 0
    def __init__(self, sp_limit, *args, **kwargs):
        super(SPForm, self).__init__(*args, **kwargs)
        self.sp_limit = sp_limit

    pilot = IntegerField("Pilot", validators=[DataRequired(), NumberRange(min=1)])
    fighter = IntegerField("Fighter", validators=[DataRequired(), NumberRange(min=1)])
    merchant = IntegerField("Merchant", validators=[DataRequired(), NumberRange(min=1)])
    engineer = IntegerField("Engineer", validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Continue")

    def validate(self):
        if not super(SPForm, self).validate():
            return False
        if (self.pilot.data + self.fighter.data + self.merchant.data + self.engineer.data) <= self.sp_limit:
            return True
        self.engineer.errors.append("Total skillpoints cannot be over " +str(self.sp_limit)+".")
        return False


class ConfirmForm(FlaskForm):
    submit = SubmitField("Confirm")
