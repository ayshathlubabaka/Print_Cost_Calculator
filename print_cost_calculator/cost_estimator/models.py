from django.db import models
from django.utils.translation import gettext_lazy as _


# Predefined Units of Measurement
UOM_CHOICES = [
    ('NO', _('No\'s')),
    ('ROLL', _('Roll')),
    ('PCS', _('Pcs')),
    ('SQM', _('SqM')),
]

# Substrate model
class Substrate(models.Model):
    name = models.CharField(_("Substrate Name"), max_length=100)  # Field for the name of the substrate
    uom = models.CharField(_("Unit of Measurement"), max_length=50)  # Field for the unit of measurement (UOM)
    status = models.BooleanField(_("Status"), default=True)  # Field for status (active/inactive)

    def __str__(self):
        return f"{self.name} ({self.uom})"


class SubstrateSize(models.Model):
    width = models.PositiveIntegerField(verbose_name=_("Width (cm)"))
    height = models.PositiveIntegerField(verbose_name=_("Height (cm)"))
    status = models.BooleanField(default=True, verbose_name=_("Status"))  # Active or Inactive

    def __str__(self):
        return f'{self.width} x {self.height}'


class SubstrateThickness(models.Model):
    value = models.PositiveIntegerField(verbose_name=_("Thickness (gsm)"))  # Store thickness value with precision
    status = models.BooleanField(default=True)  # Status: True for active, False for inactive

    def __str__(self):
        return f"Thickness: {self.value} GSM (Active)" if self.status else f"Thickness: {self.value} GSM (Inactive)"


# Product model
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Product Name"))
    uom = models.CharField(max_length=10, choices=UOM_CHOICES, verbose_name=_("Unit of Measurement"))
    status = models.BooleanField(default=True, verbose_name=_("Status"))  # Active or Inactive

    def __str__(self):
        return self.name


# Product Size Master
class ProductSize(models.Model):
    width = models.PositiveIntegerField(verbose_name=_("Width (cm)"))
    height = models.PositiveIntegerField(verbose_name=_("Height (cm)"))
    status = models.BooleanField(default=True, verbose_name=_("Status"))  # Active or Inactive

    def __str__(self):
        return f'{self.width} x {self.height}'


# Product Configuration Master
class ProductConfiguration(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    uom = models.CharField(max_length=10, choices=UOM_CHOICES, verbose_name=_("Unit of Measurement"))
    min_order_quantity = models.PositiveIntegerField(verbose_name=_("Minimum Order Quantity"))
    sizes = models.ManyToManyField(ProductSize, related_name='configurations', verbose_name=_("Product Sizes"))

    def __str__(self):
        return f'{self.product.name} Config'


# Paper Specification Master
class PaperSpecification(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Paper Specification Name"))
    status = models.BooleanField(default=True, verbose_name=_("Status"))  # Active or Inactive

    def __str__(self):
        return self.name


# Paper Configuration Master
class PaperConfiguration(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, verbose_name=_("Size"))

    def __str__(self):
        return f'{self.product.name} - {self.size}'


# Paper Configuration Detail Master
class PaperConfigurationDetail(models.Model):
    configuration = models.ForeignKey(PaperConfiguration, on_delete=models.CASCADE, related_name='details')
    paper_specifications = models.ManyToManyField(PaperSpecification, verbose_name=_("Paper Specifications"))
    max_output_quantity = models.PositiveIntegerField(verbose_name=_("Maximum Output Quantity"))

    def __str__(self):
        return f"Detail for {self.configuration}"


class SubstrateConfiguration(models.Model):
    substrate = models.ForeignKey(Substrate, on_delete=models.CASCADE)
    substrate_size = models.ForeignKey(SubstrateSize, on_delete=models.CASCADE)
    substrate_thickness = models.ForeignKey(SubstrateThickness, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.substrate.name} - {self.substrate_size.width}x{self.substrate_size.height} cm - {self.substrate_thickness.value} GSM"


class SubstrateConfigurationDetail(models.Model):
    configuration = models.ForeignKey(SubstrateConfiguration, on_delete=models.CASCADE, related_name='details')
    paper_size = models.ForeignKey(PaperSpecification, on_delete=models.CASCADE)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_output = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for {self.configuration}, Paper Size: {self.paper_size}, Cost: {self.cost_per_unit}, Max Output: {self.maximum_output}"
