from django import forms

from Remote_User.models import ClientRegister_Model


class ClientRegister_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    phoneno = forms.CharField(max_length=15, required=True)  # Add validation

    class Meta:
        model = ClientRegister_Model
        fields = ("username","email","password","phoneno","country","state","city")

