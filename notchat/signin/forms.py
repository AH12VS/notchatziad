from django import forms

class SigninForm(forms.Form):
    email = forms.CharField(
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
