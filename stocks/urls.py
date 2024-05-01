from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.StockList.as_view(), name='stock-list'),
    path('stock/<int:pk>/', views.StockDetail.as_view(), name='stock-detail'),
    path('stock/create/', views.StockCreate.as_view(), name='stock-create'),
    path('stock/update/<int:pk>/', views.StockUpdate.as_view(), name='stock-update'),
    path('stock/delete/<int:pk>/', views.StockDelete.as_view(), name='stock-delete'),
]
