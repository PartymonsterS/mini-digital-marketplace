from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "title",
            "short_description",
            "description",
            "price",
            "preview_image",
            "file",
            "status",
        )


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "title",
            "short_description",
            "description",
            "price",
            "preview_image",
            "file",
            "status",
        )