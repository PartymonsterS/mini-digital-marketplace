from django.urls import path
from .views import (
    HomeView,
    CategoryProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    MyProductsView,
)

app_name = "products"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<slug:slug>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<slug:slug>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("my-products/", MyProductsView.as_view(), name="my_products"),
    path("categories/<slug:slug>/", CategoryProductListView.as_view(), name="category_products"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
]