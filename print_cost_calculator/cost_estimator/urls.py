from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('conf_settings',views.conf_settings, name='conf_settings'),
    path('new_calculation/', views.new_calculation, name='new_calculation'),
    path('admin_calculation/', views.admin_calculation, name='admin_calculation'),
    path('user_calculation/', views.user_calculation, name='user_calculation'),
    path('new_products/', views.new_products, name='new_products'),
    path('new_product_sizes/', views.new_product_sizes, name='new_product_sizes'),
    path('new_substrate/', views.new_substrate, name='new_substrate'),

    path('substrate_list/',views.substrate_list, name='substrate_list'),
    path('create_substrate/',views.create_substrate, name='create_substrate'),
    path('update_substrate/<int:id>/',views.update_substrate, name='update_substrate'),
    path('delete_substrate/<int:id>/',views.delete_substrate, name='delete_substrate'),

    path('substrate_size_list/',views.substrate_size_list, name='substrate_size_list'),
    path('create_substrate_size/',views.create_substrate_size, name='create_substrate_size'),
    path('update_substrate_size/<int:id>/',views.update_substrate_size, name='update_substrate_size'),
    path('delete_substrate_size/<int:id>/',views.delete_substrate_size, name='delete_substrate_size'),

    path('substrate_thickness_list/',views.substrate_thickness_list, name='substrate_thickness_list'),
    path('create_substrate_thickness/',views.create_substrate_thickness, name='create_substrate_thickness'),
    path('update_substrate_thickness/<int:id>/',views.update_substrate_thickness, name='update_substrate_thickness'),
    path('delete_substrate_thickness/<int:id>/',views.delete_substrate_thickness, name='delete_substrate_thickness'),

    path('substrate_configuration_list/',views.substrate_configuration_list, name='substrate_configuration_list'),
    path('create_substrate_configuration/',views.create_substrate_configuration, name='create_substrate_configuration'),
    path('update_substrate_configuration/<int:id>/',views.update_substrate_configuration, name='update_substrate_configuration'),
    path('delete_substrate_configuration/<int:id>/',views.delete_substrate_configuration, name='delete_substrate_configuration'),

    path('paper_specification_list/',views.paper_specification_list, name='paper_specification_list'),
    path('create_paper_specification/',views.create_paper_specification, name='create_paper_specification'),
    path('update_paper_specification/<int:id>/',views.update_paper_specification, name='update_paper_specification'),
    path('delete_paper_specification/<int:id>/',views.delete_paper_specification, name='delete_paper_specification'),

    path('paper_configuration_list/',views.paper_configuration_list, name='paper_configuration_list'),
    path('create_paper_configuration/',views.create_paper_configuration, name='create_paper_configuration'),
    path('update_paper_configuration/<int:id>/',views.update_paper_configuration, name='update_paper_configuration'),
    path('delete_paper_configuration/<int:id>/',views.delete_paper_configuration, name='delete_paper_configuration'),

    path('product_list/',views.product_list, name='product_list'),
    path('create_product/',views.create_product, name='create_product'),
    path('update_product/<int:id>/',views.update_product, name='update_product'),
    path('delete_product/<int:id>/',views.delete_product, name='delete_product'),

    path('product_size_list/',views.product_size_list, name='product_size_list'),
    path('create_product_size/',views.create_product_size, name='create_product_size'),
    path('update_product_size/<int:id>/',views.update_product_size, name='update_product_size'),
    path('delete_product_size/<int:id>/',views.delete_product_size, name='delete_product_size'),

    path('product_configuration_list/',views.product_configuration_list, name='product_configuration_list'),
    path('create_product_configuration/',views.create_product_configuration, name='create_product_configuration'),
    path('update_product_configuration/<int:id>/',views.update_product_configuration, name='update_product_configuration'),
    path('delete_product_configuration/<int:id>/',views.delete_product_configuration, name='delete_product_configuration'),

]