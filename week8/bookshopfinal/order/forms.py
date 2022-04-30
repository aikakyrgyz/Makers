from django import forms
from main.models import Book

from .models import Order

#creating with class Form:
'''
class CreateOrderForm(forms.Form):
    book = forms.ModelChoiceField(Book.objects.all())
    phone = forms.CharField(max_length=30)
    address = forms.CharField(widget = forms.Textarea) # no need to specify the max length
    city = forms.CharField(max_length=100)
    email = forms.EmailField()
'''

#
# # creating with the class ModelForm:
class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    def clean_phone(self):
        data = self.cleaned_data
        phone = data.get('phone')
        print(phone)
        if not phone.startswith('+996'):
            raise forms.ValidationError('Number should start with +996')
        if len(phone) != 13:
            raise forms.ValidationError('Invalid phone number')
        return phone