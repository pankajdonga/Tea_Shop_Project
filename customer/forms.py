from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordResetForm
from customer.models import *

class CustomuserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['full_name','email','password1','password2','is_customer','is_staff','is_admin']

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['full_name','email']

class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model=CustomUser
        fields=['email'] 

class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields='__all__'

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields=['full_name','email','mobile']

class OrderForm(forms.ModelForm):
    class Meta:
        model=cart_order
        fields='__all__'

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model=cart_order
        fields=['order_status']

class UpdateDeliveryForm(forms.ModelForm):
    class Meta:
        model=cart_order
        fields=['delivery_status']

