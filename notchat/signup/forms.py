from django import forms
from users.models import UserModel


class SignupForm(forms.Form):
    email = forms.EmailField(
        min_length="3",
        max_length="250",
        widget=forms.EmailInput(),
        required=True,
        error_messages={
            "min_length": "Please enter a valid Email",
            "max_length": "Please enter a valid Email",
            "required": "Please enter a valid Email",
        },
    )
    username = forms.CharField(
        label="User Name",
        max_length="250",
        required=False,
        error_messages={
            "max_length": "Please Enter a User Name less than 250 characters",
        },
    )
    passwd = forms.CharField(
        min_length="4",
        max_length="30",
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            "min_length": "Password should be between 4 to 30 characters",
            "max_length": "Password should be between 4 to 30 characters",
            "required": "Password should be between 4 to 30 characters",
        },
    )
    confirm_passwd = forms.CharField(
        min_length="4",
        max_length="30",
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            "min_length": "Password should be between 4 to 30 characters",
            "max_length": "Password should be between 4 to 30 characters",
            "required": "Password should be between 4 to 30 characters",
        },
    )

    def clean_email(self):
        data = self.cleaned_data["email"]
        if UserModel.objects.filter(email=data).exists():
            raise forms.ValidationError("An account exists with same email address")
        return data

    def clean_confirm_passwd(self):
        passwd = self.cleaned_data["passwd"]
        confirm_passwd = self.cleaned_data["confirm_passwd"]
        if str(passwd) != str(confirm_passwd):
            raise forms.ValidationError("Confirm Password should be same to Password")

        return confirm_passwd
