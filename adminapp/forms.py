from django import forms
from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import Product


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('is_active',)

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
