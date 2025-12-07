from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Add a simple friendly password hint in the form
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="🔒 Please use a strong password (minimum 6 characters recommended)."
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age")

    # Minimal backend validation: password at least 6 characters
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")
        return password


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "age")
