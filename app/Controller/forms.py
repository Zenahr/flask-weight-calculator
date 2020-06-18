from wtforms import Form, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError

# ✅
class weightValueForm(Form):
    weightValue = FloatField('Weight', validators=[InputRequired()])

    def validate_weightValue(self, weightValue):
        regex_1 = r'\d\d\d.\d\d' # 000.00
        regex_2 = r'\d\d\d.\d'   # 000.0
        regex_3 = r'\d\d.\d\d'   # 00.00
        regex_4 = r'\d\d.\d'     # 00.0
        regex_5 = r'\d\d\d'      # 000
        regex_5 = r'\d\d'        # 00
        

        # sanitize , -> .
        value = weightValue.replace(',','.')
        
        # If regex fails
        raise ValidationError()


# ✅
class goalWeightForm(Form):
    goalWeight = FloatField('Amount', validators=[InputRequired()])



# Test ----------------------------------------------------------------------------

# form = weightValueForm()
# form.process(Amount='2.0')
# print(form.validate())

