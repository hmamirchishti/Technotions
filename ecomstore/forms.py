from django import forms
from models import Product


class ProductFormAdmin(forms.ModelForm):
    class Meta:
        model = Product
        def clean_price(self):
            if self.cleaned_data['price'] <= 0
                raise forms.ValidationError('Price must be greater than zero.')
            return self.clean_data['price']