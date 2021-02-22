from django import forms
from django.forms import ModelForm
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
