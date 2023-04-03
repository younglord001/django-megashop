from django.urls import path
from . import views

urlpatterns = [
    path('', views.producthome, name='home'),
    path('products/<product>/', views.product_cat),  #suit product category
    path('signup/', views.signup, name='sign'), #signup product  page
]