from django.urls import path
from . import views

urlpatterns = [
    path('branches/', views.BranchList.as_view(), name='branch-list'),
    path('branch/<int:pk>/', views.BranchDetail.as_view(), name='branch-detail'),
    path('branch/create/', views.BranchCreate.as_view(), name='branch-create'),
    path('branch/update/<int:pk>/', views.BranchUpdate.as_view(), name='branch-update'),
    path('branch/delete/<int:pk>/', views.BranchDelete.as_view(), name='branch-delete'),
]