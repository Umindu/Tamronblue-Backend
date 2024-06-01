from django.urls import path
from . import views

urlpatterns = [
    path('lands-plants/', views.LandPlantList.as_view(), name='land-plant-list'),
    path('land-plant-by-land/<int:land_id>/', views.LandPlantDetailByLand.as_view(), name='land-plant-detail-by-land'),
    path('land-plant/<int:pk>/', views.LandPlantDetail.as_view(), name='land-plant-detail'),
    path('land-plant/create/', views.LandPlantCreate.as_view(), name='land-plant-create'),
    path('land-plant/update/<int:pk>/', views.LandPlantUpdate.as_view(), name='land-plant-update'),
    path('land-plant/delete/<int:pk>/', views.LandPlantDelete.as_view(), name='land-plant-delete'),
]
