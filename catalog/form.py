from django import forms

from catalog.models import Product, Blog


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image',
                  'category', 'price', 'date_create', 'date_change']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['head', 'body', 'preview', 'date_create']
