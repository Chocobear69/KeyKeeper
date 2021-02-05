from django import forms


class CreateDataForm(forms.Form):
    ...


class EditDataForm(forms.Form):
    service = forms.CharField(max_length=50, label="service")
    login = forms.CharField(max_length=50, label="login")
    password = forms.PasswordInput()


class DeleteDataForm(forms.Form):
    ...
