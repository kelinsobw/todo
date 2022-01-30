from threading import current_thread
from django import forms
from django.http import request


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000)


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
