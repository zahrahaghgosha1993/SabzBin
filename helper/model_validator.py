import re

from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_phone(value):
    """
    A validator to check phone number entered is valid
    """

    regex = re.compile(r'09\d{9}$')
    search_result = regex.findall(value)

    if not search_result:
        raise ValidationError(_("Please enter a valid phone start with 09"))

    return search_result[0]
