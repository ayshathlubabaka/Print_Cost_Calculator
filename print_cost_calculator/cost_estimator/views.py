from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ProductSize, PaperSpecification, PaperConfiguration
from .forms import ProductForm, ProductSizeForm, PaperSpecificationForm, PaperConfigurationForm


def home(request):
    return render(request, 'landing.html')

def conf_settings(request):
    return render(request, 'settings.html')

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'prod.html', {'products': products})

