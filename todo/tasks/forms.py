from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime


from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        fields = '__all__'

class ApplicationForm(forms.ModelForm):

    def clean_open(self):
        currentDate = datetime.datetime.now()
        closeTime = datetime.datetime.strptime(self.data['close_time'], '%Y-%m-%d')
        openTime = datetime.datetime.strptime(self.data['open_time'], '%Y-%m-%d')
        return closeTime >= currentDate > openTime

    class Meta:
        model = Application
        fields = ('name', 'open_time', 'close_time', 'url', 'open')

class NewUserForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
