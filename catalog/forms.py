from django.forms import ModelForm

from catalog.models import Product
from django.core.exceptions import ValidationError
import os
from dotenv import load_dotenv

load_dotenv(override=True)
BAD_WORDS = os.getenv('BAD_WORDS')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name_product', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name_product'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Введите название продукта',
            'label':'Название продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта',
            'label':'Описание продукта'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'label': 'Цена продукта'
        })

    def clean(self):
        cleaned_data = super().clean()
        name_product = cleaned_data.get('name_product')
        description = cleaned_data.get('description')

        for word in BAD_WORDS:

            if word in name_product.lower():
                self.add_error('name_product', 'В названии продукта не должен содержаться спам')

            if word in description.lower():
                self.add_error('description', 'В описание продукта не должен содержаться спам')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Price не может быть отрицательным')
        return price