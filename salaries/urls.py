from django.urls import path
from . import views

urlpatterns = [
    path('salaries/', views.SalaryList.as_view(), name='salary-list'),
    path('salary/<int:pk>/', views.SalaryDetail.as_view(), name='salary-detail'),
    path('salary/create/', views.SalaryCreate.as_view(), name='salary-create'),
    path('salary/update/<int:pk>/', views.SalaryUpdate.as_view(), name='salary-update'),
    path('salary/delete/<int:pk>/', views.SalaryDelete.as_view(), name='salary-delete'),
]