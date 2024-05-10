from .models import OrderCodes
from django import forms


class IMPORT_EXCEL(forms.Form):
    class Meta:
        model = OrderCodes
        fields = '__all__'