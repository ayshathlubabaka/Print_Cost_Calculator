from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *


def home(request):
    return render(request, 'landing.html')

def conf_settings(request):
    return render(request, 'settings.html')

# Create and list Substrates
def create_substrate(request):
    if request.method == 'POST':
        form = SubstrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('substrate_list')
    else:
        form = SubstrateForm()
    
    return render(request, 'sub.html', {'form': form})

def substrate_list(request):
    substrates = Substrate.objects.filter(status=True)  # List only active substrates
    return render(request, 'sub.html', {'substrates': substrates})

# Update Substrate
def update_substrate(request, pk):
    substrate = Substrate.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SubstrateForm(request.POST, instance=substrate)
        if form.is_valid():
            form.save()
            return redirect('substrate_list')
    else:
        form = SubstrateForm(instance=substrate)
    
    return render(request, 'sub.html', {'form': form})

# Create and list SubstrateSizes
def create_substrate_size(request):
    if request.method == 'POST':
        form = SubstrateSizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('substrate_size_list')
    else:
        form = SubstrateSizeForm()
    
    return render(request, 'sub_sizes.html', {'form': form})

def substrate_size_list(request):
    sizes = SubstrateSize.objects.filter(status=True)  # List only active sizes
    return render(request, 'sub_sizes.html', {'sizes': sizes})

# Update SubstrateSize
def update_substrate_size(request, pk):
    substrate_size = SubstrateSize.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SubstrateSizeForm(request.POST, instance=substrate_size)
        if form.is_valid():
            form.save()
            return redirect('substrate_size_list')
    else:
        form = SubstrateSizeForm(instance=substrate_size)
    
    return render(request, 'update_substrate_size.html', {'form': form})

# Create and list SubstrateThicknesses
def create_substrate_thickness(request):
    if request.method == 'POST':
        form = SubstrateThicknessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('substrate_thickness_list')
    else:
        form = SubstrateThicknessForm()
    
    return render(request, 'create_substrate_thickness.html', {'form': form})

def substrate_thickness_list(request):
    thicknesses = SubstrateThickness.objects.filter(status=True)  # List only active thicknesses
    return render(request, 'substrate_thickness_list.html', {'thicknesses': thicknesses})


# Update SubstrateThickness
def update_substrate_thickness(request, pk):
    substrate_thickness = SubstrateThickness.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = SubstrateThicknessForm(request.POST, instance=substrate_thickness)
        if form.is_valid():
            form.save()
            return redirect('substrate_thickness_list')
    else:
        form = SubstrateThicknessForm(instance=substrate_thickness)
    
    return render(request, 'update_substrate_thickness.html', {'form': form})

# Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

# Product Create View
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list after saving
    else:
        form = ProductForm()
    return render(request, 'product/product_form.html', {'form': form})

# Product Update View
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list after saving
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_form.html', {'form': form})

# Product Size List View
def product_size_list(request):
    sizes = ProductSize.objects.all()
    return render(request, 'product/product_size_list.html', {'sizes': sizes})

# Product Size Create View
def product_size_create(request):
    if request.method == 'POST':
        form = ProductSizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_size_list')  # Redirect to product size list after saving
    else:
        form = ProductSizeForm()
    return render(request, 'product/product_size_form.html', {'form': form})

# Product Size Update View
def product_size_update(request, pk):
    size = get_object_or_404(ProductSize, pk=pk)
    if request.method == 'POST':
        form = ProductSizeForm(request.POST, instance=size)
        if form.is_valid():
            form.save()
            return redirect('product_size_list')  # Redirect to product size list after saving
    else:
        form = ProductSizeForm(instance=size)
    return render(request, 'product/product_size_form.html', {'form': form})

# Product Configuration List View
def product_configuration_list(request):
    configurations = ProductConfiguration.objects.all()
    return render(request, 'product/product_configuration_list.html', {'configurations': configurations})

# Product Configuration Create View
def product_configuration_create(request):
    if request.method == 'POST':
        form = ProductConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_configuration_list')  # Redirect to product configuration list after saving
    else:
        form = ProductConfigurationForm()
    return render(request, 'product/product_configuration_form.html', {'form': form})

# Product Configuration Update View
def product_configuration_update(request, pk):
    configuration = get_object_or_404(ProductConfiguration, pk=pk)
    if request.method == 'POST':
        form = ProductConfigurationForm(request.POST, instance=configuration)
        if form.is_valid():
            form.save()
            return redirect('product_configuration_list')  # Redirect to product configuration list after saving
    else:
        form = ProductConfigurationForm(instance=configuration)
    return render(request, 'product/product_configuration_form.html', {'form': form})
