import re
from django.core.exceptions import ValidationError


class PasswordValidator:
    def validate(self,password,user=None):
        if not re.findall('A-Z',password):
            raise ValidationError('Password must contain at least 1 uppercase letter, A-Z.')
        if not re.findall('a-z',password):
            raise ValidationError('Password must contain at least 1 lowercase letter, a-z.')
        if not re.findall('0-9',password):
            raise ValidationError('Password must contain at least 1 digit, 0-9.')
        if not re.findall('[^A-Za-z0-9]',password):
            raise ValidationError('Password must contain at least 1 special character (e.g. @, #, $).')
        
    def response(self):
        return "Your password must contain at least one uppercase letter, one lowercase letter, one number, and one special character."