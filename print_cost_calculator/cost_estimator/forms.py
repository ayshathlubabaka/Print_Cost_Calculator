from django import forms
from .models import *

class SubstrateForm(forms.ModelForm):
    class Meta:
        model = Substrate
        fields = ['name', 'uom', 'status']  # Include status field to allow editing

class SubstrateSizeForm(forms.ModelForm):
    class Meta:
        model = SubstrateSize
        fields = ['size', 'status']  # Include status field to allow editing

class SubstrateThicknessForm(forms.ModelForm):
    class Meta:
        model = SubstrateThickness
        fields = ['value', 'status']  # Include status field to allow editing

class PaperSpecificationForm(forms.ModelForm):
    class Meta:
        model = PaperSpecification
        fields = ['name', 'status']

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'uom', 'status']

# Product Size Form
class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ['size', 'status']

# Product Configuration Form
class ProductConfigurationForm(forms.ModelForm):
    class Meta:
        model = ProductConfiguration
        fields = ['product', 'uom', 'min_order_quantity', 'sizes']

# Form for Paper Configuration
class PaperConfigurationForm(forms.ModelForm):
    class Meta:
        model = PaperConfiguration
        fields = ['product', 'size', 'paper_specification', 'max_output_quantity']  # Include all fields in the PaperConfiguration model

class SubstrateConfigurationForm(forms.ModelForm):
    class Meta:
        model = SubstrateConfiguration
        fields = ['substrate', 'substrate_size', 'substrate_thickness', 'paper_size', 'cost_per_unit', 'maximum_output', 'total']
