from django import forms

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    """Общий стиль форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления продукта"""

    class Meta:
        model = Product
        exclude = ('user',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for data in cleaned_data.split(' '):
            if data in FORBIDDEN_WORDS:
                raise forms.ValidationError('Ошибка валидации. Некоррекное название')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Форма добавления версии продукта"""

    class Meta:
        model = Version
        fields = '__all__'


