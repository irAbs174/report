from .models import OrderCodes
from django import forms
from attr import fields


class IMPORT_EXCEL(forms.Form):
    class Meta:
        model = OrderCodes
        fields = '__all__'