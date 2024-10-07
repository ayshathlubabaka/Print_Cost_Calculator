from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('conf_settings',views.conf_settings, name='conf_settings'),
    path('substrate_list/',views.substrate_list, name='substrate_list'),
    path('create_substrate/',views.create_substrate, name='create_substrate'),
    path('update_substrate/<int:id>/',views.update_substrate, name='update_substrate'),
    path('substrate_size_list/',views.substrate_size_list, name='substrate_size_list'),
    path('create_substrate_size/',views.create_substrate_size, name='create_substrate_size'),
    path('update_substrate_size/<int:id>/',views.update_substrate_size, name='update_substrate_size'),
    path('substrate_thickness_list/',views.substrate_thickness_list, name='substrate_thickness_list'),
    path('create_substrate_thickness/',views.create_substrate_thickness, name='create_substrate_thickness'),
    path('update_substrate_thickness/<int:id>/',views.update_substrate_thickness, name='update_substrate_thickness'),
    path('paper_specification_list/',views.paper_specification_list, name='paper_specification_list'),
    path('create_paper_specification/',views.create_paper_specification, name='create_paper_specification'),
    path('update_paper_specification/',views.update_paper_specification, name='update_paper_specification'),
    path('product_list/',views.product_list, name='product_list'),
    path('create_product/',views.create_product, name='create_product'),
    path('product_size_list/',views.product_size_list, name='product_size_list'),
    path('create_product_size/',views.create_product_size, name='create_product_size'),
    path('product_configuration_list/',views.product_configuration_list, name='product_configuration_list'),
    path('create_product_configuration/',views.create_product_configuration, name='create_product_configuration'),
    path('paper_configuration_list/',views.paper_configuration_list, name='paper_configuration_list'),
    path('create_paper_configuration/',views.create_paper_configuration, name='create_paper_configuration'),
    path('substrate_configuration_list/',views.substrate_configuration_list, name='substrate_configuration_list'),
    path('create_substrate_configuration/',views.create_substrate_configuration, name='create_substrate_configuration'),
]