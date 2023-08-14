from django import forms

from catalog.models import Product, Blog


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for data in cleaned_data.split(' '):
            if data in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
                raise forms.ValidationError('Ошибка валидации. Некоррекное название')
        return cleaned_data


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
