from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Student

class AdminUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"password/\">this form</a>."
    )

    class Meta:
        model = Student
        fields = (
            'email', 'first_name', 'last_name',
        )

    def clean_password(self):
        ...
        return self.initial["password"]