from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *


def home(request):
    return render(request, 'landing.html')

def conf_settings(request):
    return render(request, 'settings.html')

def create_substrate(request):
    if request.method == 'POST':
        form = SubstrateForm(request.POST)
        if form.is_valid():
            substrate = form.save(commit=False)  # Don't save yet
            substrate.status = True  # Set the status to True
            substrate.save()  # Now save the substrate
            messages.success(request, 'Substrate created successfully!')  # Add a success message
            return redirect('substrate_list')  # Redirect to the list view after successful save
    else:
        form = SubstrateForm()  # Create a new form instance for GET requests

    return render(request, 'sub.html', {'form': form})  # Render the form in the template

def substrate_list(request):
    substrates = Substrate.objects.all()
    return render(request, 'sub.html', {'substrates': substrates})

# Update Substrate
def update_substrate(request, id):
    substrate = Substrate.objects.get(id=id)
    
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
    print(request)
    if request.method == 'POST':
        form = SubstrateSizeForm(request.POST)
        if form.is_valid():
            substrate_size = form.save(commit=False)  # Don't save yet
            substrate_size.status = True  # Set the status to True
            substrate_size.save()
            return redirect('substrate_size_list')
    else:
        form = SubstrateSizeForm()
    
    return render(request, 'subsizes.html', {'form': form})

def substrate_size_list(request):
    sizes = SubstrateSize.objects.all()
    return render(request, 'subsizes.html', {'sizes': sizes})

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
            substrate_thickness = form.save(commit=False)  # Don't save yet
            substrate_thickness.status = True  # Set the status to True
            substrate_thickness.save()
            return redirect('substrate_thickness_list')
    else:
        form = SubstrateThicknessForm()
    
    return render(request, 'gsm.html', {'form': form})

def substrate_thickness_list(request):
    thicknesses = SubstrateThickness.objects.all() 
    return render(request, 'gsm.html', {'thicknesses': thicknesses})


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

def create_paper_specification(request):
    if request.method == 'POST':
        form = PaperSpecificationForm(request.POST)
        if form.is_valid():
            paper_specification = form.save(commit=False)  # Don't save yet
            paper_specification.status = True  # Set the status to True
            paper_specification.save()  # Save the model instance
            return redirect('paper_specification_list')  # Redirect to the list view after successful save
    else:
        form = PaperSpecificationForm()  # Create a new form instance for GET requests

    return render(request, 'paper_sizes.html', {'form': form})  # Render the form in the template

def paper_specification_list(request):
    paper_specifications = PaperSpecification.objects.all()  # Retrieve all paper specifications
    return render(request, 'papersizes.html', {'paper_specifications': paper_specifications})  # Render the list in the template

def update_paper_specification(request, pk):
    paper_specification = get_object_or_404(PaperSpecification, pk=pk)  # Retrieve the specific instance
    
    if request.method == 'POST':
        form = PaperSpecificationForm(request.POST, instance=paper_specification)  # Bind the form with the instance
        if form.is_valid():
            form.save()  # Save the updated instance
            return redirect('paper_specification_list')  # Redirect to the list view after update
    else:
        form = PaperSpecificationForm(instance=paper_specification)  # Create a form instance with existing data

    return render(request, 'update_paper_specification.html', {'form': form})  # Render the update form

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
def product_size_update(request, id):
    size = get_object_or_404(ProductSize, id=id)
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
