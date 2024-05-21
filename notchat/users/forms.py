from django import forms


class AccountForm(forms.Form):
    email = forms.EmailField(
        min_length="3",
        max_length="250",
        widget=forms.EmailInput(),
        required=False,
        disabled=True,
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

    img_prof = forms.ImageField(
        label="Image",
        required=False,
    )

    def clean_confirm_passwd(self):
        passwd = self.cleaned_data["passwd"]
        confirm_passwd = self.cleaned_data["confirm_passwd"]
        if str(passwd) != str(confirm_passwd):
            raise forms.ValidationError("Confirm Password should be same to Password")

        return confirm_passwd
