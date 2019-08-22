from django import forms
from .models import BankDetails


class Updateform(forms.ModelForm):
    ifsc = forms.CharField(min_length=11, max_length=20, required=True,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Enter IFSC.'
                           }))

    class Meta:
        model = BankDetails
        fields = ['ifsc']


class DetailForm(forms.ModelForm):
    bank_name = forms.CharField(min_length=10,max_length=50,
                                widget=forms.TextInput(attrs={
                                    'placeholder':'ENTER BANK NAME'
                                }))
    city = forms.CharField(min_length=5,max_length=50,
                           widget=forms.TextInput(attrs={
                               'placeholder':'ENTER CITY'
                           }))

    class Meta:
        model = BankDetails
        fields = ['bank_name']
