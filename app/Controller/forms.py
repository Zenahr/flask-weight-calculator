from wtforms import Form, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError
import re

# ✅
class weightValueForm(Form):
    weightValue = FloatField('Weight', validators=[InputRequired()])

    def validate_weightValue(self, weightValue):

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
            match = re.search(regex, weightValue)
            if match:
                return weightValue
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

    weightValue = str(weightValue)

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
        match = re.search(regex, weightValue)
        if match and not len(weightValue) > 5:
            print("match")
            return weightValue
    print("no match")
    raise ValidationError("bad input")

validate_weightValue(9000)