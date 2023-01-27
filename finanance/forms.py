from django import forms
from django.contrib.auth.models import User
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class ClientForm(forms.ModelForm):
    class Meta:
        model=models.Client
        fields=['Name','address','mobile','Type']
        
class TypeForm(forms.ModelForm):
    class Meta:
        model=models.Type
        fields=['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Produit
        fields=['produit','libelle','quantity','prix']

class FactForm(forms.ModelForm):
    class Meta:
        model=models.Facture
        fields=['code','client','fournisseur','produit','date_facturation','HTaxe','Total']

# #address of shipment
# class AddressForm(forms.Form):
#     Email = forms.EmailField()
#     Mobile= forms.IntegerField()
#     Address = forms.CharField(max_length=500)

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model=models.Feedback
#         fields=['name','feedback']

# #for updating status of order
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model=models.Orders
#         fields=['status']

# #for contact us page
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
