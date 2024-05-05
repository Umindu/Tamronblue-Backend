from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile-create'),
    path('profile/update/<int:pk>/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profile/delete/<int:pk>/', views.ProfileDelete.as_view(), name='profile-delete'),
]