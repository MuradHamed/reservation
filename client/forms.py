from django import forms
from .models import Client, ClientTypes, Product, Order

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.ChoiceField(choices=[('Food', 'Food'), ('Snacks', 'Snacks'), ('Drinks', 'Drinks'), ('Hardware', 'Hardware')])
    description = forms.CharField(widget=forms.Textarea)
    rating = forms.FloatField()


class ClientForm(forms.Form):
    class Meta:
        model = Client
        fields = '__all__'

class ClientTypesForm(forms.Form):
    class Meta:
        model = ClientTypes
        fields = '__all__'

class OrderForm(forms.Form):
    class Meta:
        model = Order
        fields = '__all__'
