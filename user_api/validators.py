from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

MIN_LENGTH = 1
SPECIAL_CHARACTERS = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"


def password_validate(password):
    errors = []
    if not any(char.isdigit() for char in password):
        errors.append(f'Password must contain at least {MIN_LENGTH} digit.')
    if not any(char.isalpha() for char in password):
        errors.append(f'Password must contain at least {MIN_LENGTH} letter.')
    if not any(char.isupper() for char in password):
        errors.append(f'Password must contain at least {MIN_LENGTH} upper letter.')
    if not any(char in SPECIAL_CHARACTERS for char in password):
        errors.append(f'Password must contain at least {MIN_LENGTH} special character('
                      " ~!$@#%^&*()_+{}:;'[] ).")

    if errors:
        raise ValidationError(errors)


def email_validate(email):
    at_symbol = email.find('@')

    error = 'Your email is incorrect!'
    if at_symbol != -1:
        # take name before '@'
        url_name = email[:at_symbol]
        if any(char in SPECIAL_CHARACTERS and char not in "._" for char in url_name):
            raise ValidationError(error)
        if not any(char.isalpha() for char in url_name):
            raise ValidationError(error)

        # take name after '@' and before domain
        before_domain = email[at_symbol + 1:email.rfind('.')]
        if any(char in SPECIAL_CHARACTERS or char.isdigit() for char in before_domain):
            raise ValidationError(error)
        if not any(char.isalpha() for char in before_domain):
            raise ValidationError(error)

        # take only domains
        domains = email.split('.')
        del domains[0]

        for domain in domains:
            if any(char in SPECIAL_CHARACTERS or char.isdigit() for char in domain):
                raise ValidationError(error)
            if not any(char.isalpha() for char in domain):
                raise ValidationError(error)
    else:
        raise ValidationError(error)
