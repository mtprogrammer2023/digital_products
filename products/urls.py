from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import (
    ProductListView, ProductDetailView, CategoryListView, CategoryDetailView
    , FileListView, FileDetailView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name="product-list"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),

    path('categories/', CategoryListView.as_view(), name="category-list"),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),


    path('products/<int:product_id>/files/', FileListView.as_view(), name="file-list"),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name="file-detail")



]