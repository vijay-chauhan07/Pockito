from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .widgets import XDSoftDateTimePickerInput
from  django.core.exceptions import  ValidationError
from django.utils import timezone



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='optional')
    email = forms.EmailField(
        max_length=250, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class TodoCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=XDSoftDateTimePickerInput()

    )

    description = forms.CharField( widget=forms.Textarea())

    class Meta:
        model = Todo
        fields = ('title', 'description', 'deadline', )
    def clean(self):
        
        deadline = self.cleaned_data['deadline']
        if deadline <=timezone.now():
            raise forms.ValidationError("Deadline should be greater than now.")
        else:
            pass
        
        








class TodoUpdateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=XDSoftDateTimePickerInput()

    )

    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Describe your task'}))
    class Meta:
        model = Todo
        fields = ('title', 'description', 'deadline', )
    def clean(self):
        
        deadline = self.cleaned_data['deadline']
        if deadline <=timezone.now():
            raise forms.ValidationError("Deadline should be greater than now.")
        else:
            pass
        
        


    
    
    
    
    






class ProfileUpdateForm(forms.ModelForm):
    

    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

    