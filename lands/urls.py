from django.urls import path
from . import views

urlpatterns = [
    path('lands/', views.LandList.as_view(), name='land-list'),
    path('land/<int:pk>/', views.LandDetail.as_view(), name='land-detail'),
    path('land/create/', views.LandCreate.as_view(), name='land-create'),
    path('land/update/<int:pk>/', views.LandUpdate.as_view(), name='land-update'),
    path('land/delete/<int:pk>/', views.LandDelete.as_view(), name='land-delete'),
]