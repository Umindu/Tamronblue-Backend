from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('customer/create/', views.CustomerCreate.as_view(), name='customer-create'),
    path('customer/update/<int:pk>/', views.CustomerUpdate.as_view(), name='customer-update'),
    path('customer/delete/<int:pk>/', views.CustomerDelete.as_view(), name='customer-delete'),
]