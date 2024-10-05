from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('conf_settings',views.conf_settings, name='conf_settings'),
    path('product_list/',views.product_list, name='product_list'),
    # path('product_create/',views.product_create, name='product_create'),
    # path('product_update/',views.product_update, name='product_update'),
    # path('product_delete/',views.product_delete, name='product_delete'),
    # path('product_size_list/',views.product_size_list, name='product_size_list'),
    # path('product_size_create/',views.product_size_create, name='product_size_create'),
    # path('product_size_update/',views.product_size_update, name='product_size_update'),
    # path('product_size_delete/',views.product_size_delete, name='product_size_delete'),
    # path('paper_specification_list/',views.paper_specification_list, name='paper_specification_list'),
    # path('paper_specification_create/',views.paper_specification_create, name='paper_specification_create'),
    # path('paper_specification_update/',views.paper_specification_update, name='paper_specification_update'),
    # path('paper_specification_delete/',views.paper_specification_delete, name='paper_specification_delete'),
    # path('paper_configuration_list/',views.paper_configuration_list, name='paper_configuration_list'),
    # path('paper_configuration_create/',views.paper_configuration_create, name='paper_configuration_create'),
    # path('paper_configuration_update/',views.paper_configuration_update, name='paper_configuration_update'),
    # path('paper_configuration_delete/',views.paper_configuration_delete, name='paper_configuration_delete'),
]