from wtforms import Form, IntegerField, FloatField
from wtforms.validators import InputRequired

# ✅
class weightValueForm(Form):
    weightValue = FloatField('Amount', validators=[InputRequired()])

# ✅
class goalWeightForm(Form):
    goalWeight = FloatField('Amount', validators=[InputRequired()])



# Test ----------------------------------------------------------------------------

form = weightValueForm()
form.process(weightValueForm=2.0)
form.validate()
print(form.errors)