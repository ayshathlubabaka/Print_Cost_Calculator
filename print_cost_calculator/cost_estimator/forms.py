from django import forms
from .models import Product, ProductSize, PaperSpecification, PaperConfiguration

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  

class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = '__all__'  

class PaperSpecificationForm(forms.ModelForm):
    class Meta:
        model = PaperSpecification
        fields = '__all__' 

class PaperConfigurationForm(forms.ModelForm):
    class Meta:
        model = PaperConfiguration
        fields = '__all__'  
