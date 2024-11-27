from django import forms
from manager.models import *

class ProductModelForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields=['product_name','select_category','quantity','price','description','product_img']


class staffModelForm(forms.ModelForm):
    class Meta:
        model=staff
        fields='__all__'


class staffAttendanceForm(forms.ModelForm):
    class Meta:
        model=StaffAttendance
        fields='__all__'