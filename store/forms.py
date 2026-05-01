from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, CustomerProfile


# 🛒 PRODUCTS
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'image',   # ✅ importante para upload de foto
            'stock'
        ]


# 👤 REGISTER
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)

        # salva email no user padrão
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            # cria perfil do cliente
            CustomerProfile.objects.create(
                user=user,
                city=self.cleaned_data['city'],
                address=self.cleaned_data['address'],
                phone=self.cleaned_data['phone']
            )

        return user