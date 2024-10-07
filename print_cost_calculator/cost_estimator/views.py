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
    return render(request, 'prod.html', {'products': products})

# Products Create View
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)  # Don't save yet
            product.status = True  # Set the status to True
            product.save()  # Save the model instance
            return redirect('product_list')  # Redirect to product list after saving
        else:
            print(form.errors)
    else:
        form = ProductForm()
    
    return render(request, 'prod.html', {'form': form})  # Return the form (with errors if any)


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
    return render(request, 'prosizes.html', {'sizes': sizes})

# Product Size Create View
def create_product_size(request):
    if request.method == 'POST':
        form = ProductSizeForm(request.POST)
        if form.is_valid():
            product_size = form.save(commit=False)  # Don't save yet
            product_size.status = True  # Set the status to True
            product_size.save()  # Save the model instance
            return redirect('product_size_list')  # Redirect to product size list after saving
    else:
        form = ProductSizeForm()
    return render(request, 'prosizes.html', {'form': form})

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
    products = Product.objects.all()
    sizes = ProductSize.objects.all()
    uoms = ProductConfiguration._meta.get_field('uom').choices  # UoM choices from the model field
    return render(request, 'proconf.html', 
                  {'configurations': configurations, 
                   'products': products,
                    'sizes': sizes,
                    'uoms': uoms 
                  })

def create_product_configuration(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        uom_value = request.POST.get('uom')  # Get the selected UoM value from the form
        min_order_quantity = request.POST.get('min_order_quantity')
        selected_size_ids = request.POST.getlist('sizes')

        if product_id and uom_value and min_order_quantity and selected_size_ids:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                # Handle case where the product does not exist
                return render(request, 'proconf.html', {
                    'error': "Product not found.",
                    'products': Product.objects.all(),
                    'sizes': ProductSize.objects.all(),
                    'uoms': ProductConfiguration._meta.get_field('uom').choices
                })

            # Create and save the product configuration
            product_configuration = ProductConfiguration(
                product=product,
                uom=uom_value,  # Directly store the UoM as it’s a choice field
                min_order_quantity=min_order_quantity,
            )
            product_configuration.save()

            # Get the selected sizes and assign them
            sizes = ProductSize.objects.filter(id__in=selected_size_ids)
            product_configuration.sizes.set(sizes.values_list('id', flat=True))


            return redirect('product_configuration_list')

        else:
            # Handle missing data, re-render the form with an error message
            return render(request, 'proconf.html', {
                'error': "All fields are required.",
                'products': Product.objects.all(),
                'sizes': ProductSize.objects.all(),
                'uoms': ProductConfiguration._meta.get_field('uom').choices
            })

    # Fetch products and sizes for the form if GET request
    products = Product.objects.all()
    sizes = ProductSize.objects.all()
    uoms = ProductConfiguration._meta.get_field('uom').choices  # UoM choices from the model field

    return render(request, 'proconf.html', {
        'products': products,
        'sizes': sizes,
        'uoms': uoms
    })


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

def paper_configuration_list(request):
    # Get all configurations
    paper_configurations = PaperConfiguration.objects.select_related('product', 'size', 'paper_specification').all()  

    # Active products
    products = Product.objects.filter(status=True)  

    # Active sizes
    product_sizes = ProductSize.objects.filter(status=True)  

    # Active specifications
    paper_specifications = PaperSpecification.objects.filter(status=True)  

    return render(request, 'paperconf.html', {
        'paper_configurations': paper_configurations,
        'products': products,
        'product_sizes': product_sizes,
        'paper_specifications': paper_specifications,
    })

def create_paper_configuration(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        size = request.POST.get('size')
        
        # Get the lists of paper specifications and max output quantities
        paper_specifications = request.POST.getlist('paper_specification')
        max_output_quantities = request.POST.getlist('max_output_quantity')

        # Iterate through the details and save them
        for i in range(len(paper_specifications)):
            if paper_specifications[i]:  # Ensure the paper specification is selected
                # Create and save the configuration instance
                paper_configuration = PaperConfiguration(
                    product_id=product,
                    size_id=size,
                    paper_specification_id=paper_specifications[i],
                    max_output_quantity=max_output_quantities[i]  # Assign the quantity
                )
                paper_configuration.save()

        return redirect('paper_configuration_list')

    else:
        # If not POST, create empty form
        products = Product.objects.filter(status=True)
        product_sizes = ProductSize.objects.filter(status=True)
        paper_specifications = PaperSpecification.objects.filter(status=True)

        return render(request, 'paperconf.html', {
            'products': products,
            'product_sizes': product_sizes,
            'paper_specifications': paper_specifications,
        })
    

def substrate_configuration_list(request):
    # Fetch all substrate configurations
    substrate_configurations = SubstrateConfiguration.objects.all()

    # Fetch related models to display
    substrates = Substrate.objects.filter(status=True)  # Only active substrates
    substrate_sizes = SubstrateSize.objects.filter(status=True)  # Only active sizes
    substrate_thicknesses = SubstrateThickness.objects.filter(status=True)  # Only active thicknesses
    paper_sizes = PaperSpecification.objects.filter(status=True)  # Only active paper sizes
    print(paper_sizes)

    return render(request, 'subconf.html', {
        'substrate_configurations': substrate_configurations,
        'substrates': substrates,
        'substrate_sizes': substrate_sizes,
        'substrate_thicknesses': substrate_thicknesses,
        'paper_sizes': paper_sizes,
    })
    
def create_substrate_configuration(request):
    if request.method == 'POST':
        # Extract the main form data
        substrate = request.POST.get('substrate')
        substrate_size = request.POST.get('substrate_size')
        substrate_thickness = request.POST.get('substrate_thickness')
        paper_size = request.POST.get('paper_size')
        
        # Get the lists of cost per unit, maximum output, and total from the repeater
        cost_per_units = request.POST.getlist('cost_per_unit')
        maximum_outputs = request.POST.getlist('maximum_output')
        totals = request.POST.getlist('total')

        # Iterate through the details and save them
        for i in range(len(cost_per_units)):
            if cost_per_units[i]:  # Ensure the cost_per_unit is provided
                # Create and save the configuration instance
                substrate_configuration = SubstrateConfiguration(
                    substrate_id=substrate,
                    substrate_size_id=substrate_size,
                    substrate_thickness_id=substrate_thickness,
                    paper_size_id=paper_size,
                    cost_per_unit=cost_per_units[i],  # Assign the cost per unit
                    maximum_output=maximum_outputs[i],  # Assign the maximum output
                    total=totals[i]  # Assign the total
                )
                substrate_configuration.save()

        return redirect('substrate_configuration_list')

    else:
        # If GET, instantiate an empty form
        form = SubstrateConfigurationForm()

    # Fetch active records to display in the form
    substrates = Substrate.objects.filter(status=True)  # Only active substrates
    substrate_sizes = SubstrateSize.objects.filter(status=True)  # Only active sizes
    substrate_thicknesses = SubstrateThickness.objects.filter(status=True)  # Only active thicknesses
    paper_sizes = PaperSpecification.objects.filter(status=True)  # Only active paper sizes
    print(paper_sizes)

    return render(request, 'subconf.html', {
        'form': form,
        'substrates': substrates,
        'substrate_sizes': substrate_sizes,
        'substrate_thicknesses': substrate_thicknesses,
        'paper_sizes': paper_sizes,
    })