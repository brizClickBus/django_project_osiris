from django import forms

class Sign_up(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    repeatPassWord = forms.CharField(max_length=100,widget=forms.PasswordInput)

class Sign_in(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)