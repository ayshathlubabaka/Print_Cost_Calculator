from django.db import models
from django.utils.translation import gettext_lazy as _

# Predefined Units of Measurement
UOM_CHOICES = [
    ('NO', _('No\'s')),
    ('ROLL', _('Roll')),
    ('PCS', _('Pcs')),
    ('SQM', _('SqM')),
]

# Product model
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Product Name"))
    uom = models.CharField(max_length=10, choices=UOM_CHOICES, verbose_name=_("Unit of Measurement"))
    status = models.BooleanField(default=True, verbose_name=_("Status"))  # Active or Inactive

    def __str__(self):
        return self.name

# Product Size Master
class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes', verbose_name=_("Product"))
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Width (cm)"))
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Height (cm)"))
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
    paper_specifications = models.ManyToManyField(PaperSpecification, verbose_name=_("Paper Specifications"))
    max_output_quantity = models.PositiveIntegerField(verbose_name=_("Maximum Output Quantity"))

    def __str__(self):
        return f'{self.product.name} - {self.size}'

