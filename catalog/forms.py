from django import forms

from catalog.models import Product, Blog, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for data in cleaned_data.split(' '):
            if data in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
                raise forms.ValidationError('Ошибка валидации. Некоррекное название')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


    # def clean_is_active(self):
    #     cleaned_data = self.cleaned_data['is_active']
    #     if cleaned_data:
    #         active_version = Version.objects.filter(is_active=True)
    #         if active_version.count() >= 1:
    #             raise forms.ValidationError('Может быть только одна активная форма')
    #     return cleaned_data
    #

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
