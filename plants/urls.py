from django.urls import path
from . import views

urlpatterns = [
    path('plants/', views.PlantList.as_view(), name='plant-list'),
    path('plant/<int:pk>/', views.PlantDetail.as_view(), name='plant-detail'),
    path('plant/create/', views.PlantCreate.as_view(), name='plant-create'),
    path('plant/update/<int:pk>/', views.PlantUpdate.as_view(), name='plant-update'),
    path('plant/delete/<int:pk>/', views.PlantDelete.as_view(), name='plant-delete'),
]