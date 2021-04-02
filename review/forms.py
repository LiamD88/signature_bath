from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Name'}))
    number = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Number'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'required': 'True', 'class': 'form-control', 'placeholder': 'Message'}))



    class Meta:
        model = Review
        fields = ['name', 'number', 'email', 'message']