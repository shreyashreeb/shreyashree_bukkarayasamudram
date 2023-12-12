from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(validators=[EmailValidator()])  # Uses Django's built-in EmailValidator

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
        labels = {
            'address': 'Notes',
        }
        error_messages = {
            'email': {
                'invalid': 'Enter a valid email address with a domain.',
            },
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or "@" not in email or not email.split('@')[1].count('.') >= 1:  # Custom validation for domain
            raise ValidationError(self.Meta.error_messages['email']['invalid'])
        return email

