from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def valid_cpf_format(value):
    
    condition = re.compile(r"(?i:\b\d{1,9}[\d|X]\b)")
    result = condition.findall(value)

    tam_result = len(result)

    if tam_result != 1:
        raise ValidationError(
            _('%(value)s is not a valid CPF format'),
            params={'value': value},
        )
