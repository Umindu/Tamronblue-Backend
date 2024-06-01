from django.urls import path
from . import views

urlpatterns = [
    path('varieties/', views.VarietyList.as_view(), name='variety-list'),
    path('varieties/plant/<int:plant_id>/', views.VarietyByPlant.as_view(), name='variety-by-plant'),
    path('variety/<int:pk>/', views.VarietyDetail.as_view(), name='variety-detail'),
    path('variety/create/', views.VarietyCreate.as_view(), name='variety-create'),
    path('variety/update/<int:pk>/', views.VarietyUpdate.as_view(), name='variety-update'),
    path('variety/delete/<int:pk>/', views.VarietyDelete.as_view(), name='variety-delete'),
]