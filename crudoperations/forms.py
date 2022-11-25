from django import forms
from .models import Mytodos

class Todoform(forms.ModelForm):
    task=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Add Task','style':'width:100%'}))
    class Meta:
        model=Mytodos
        fields=['task',]