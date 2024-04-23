from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.index, name='product_index'),
    path('products/<int:id>/', views.show, name='product_show'),
]