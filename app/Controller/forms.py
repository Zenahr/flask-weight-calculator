from wtforms import Form, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError
import re

# ✅
class weightValueForm(Form):
    weightValue = FloatField('Weight', validators=[InputRequired()])

    def validate_weightValue(self, weightValue):
        
        

        # sanitize , -> .
        if "," in weightValue and not isinstance(weightValue, int) or isinstance(weightValue, float):
            value = weightValue.replace(',','.')

        """regex for all possible numbers"""
        regex_list = [
            r'^\d\d\d.\d\d$', # 000.00
            r'^\d\d\d.\d$',   # 000.0
            r'^\d\d.\d\d$',   # 00.00
            r'^\d\d.\d$',     # 00.0
            r'^\d\d\d$',      # 000
            r'^\d\d$'        # 00
        ]
        
        #regex
        for regex in regex_list:
            match = re.search(regex, value)
            if match:
                return value
            else:
                raise ValidationError("bad input")



# ✅
class goalWeightForm(Form):
    goalWeight = FloatField('Amount', validators=[InputRequired()])



# Test ----------------------------------------------------------------------------

# form = weightValueForm()
# form.process(Amount='2.0')
# print(form.validate())

def validate_weightValue(weightValue):
    """regex for all possible numbers"""
    regex_list = [
        r'^\d\d\d.\d\d$', # 000.00
        r'^\d\d\d.\d$',   # 000.0
        r'^\d\d.\d\d$',   # 00.00
        r'^\d\d.\d$',     # 00.0
        r'^\d\d\d$',      # 000
        r'^\d\d$'        # 00
    ]

    # sanitize , -> .
    value = weightValue.replace(',','.')

    #regex
    for regex in regex_list:
        match = re.search(regex, value)
        if match:
            return value
        else:
            raise ValidationError("bad input")

validate_weightValue(90)