from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Substrate)
admin.site.register(SubstrateSize)
admin.site.register(SubstrateThickness)
admin.site.register(PaperSpecification)
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ProductConfiguration)
admin.site.register(PaperConfiguration)
admin.site.register(SubstrateConfiguration)