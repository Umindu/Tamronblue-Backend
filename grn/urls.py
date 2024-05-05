from django.urls import path
from . import views

urlpatterns = [
    path('grns/', views.GrnList.as_view(), name='grn-list'),
    path('grn/<int:pk>/', views.GrnDetail.as_view(), name='grn-detail'),
    path('grn/create/', views.GrnCreate.as_view(), name='grn-create'),
    path('grn/update/<int:pk>/', views.GrnUpdate.as_view(), name='grn-update'),
    path('grn/delete/<int:pk>/', views.GrnDelete.as_view(), name='grn-delete'),

    path('grn-details/', views.GrnDetailList.as_view(), name='grn-detail-list'),
    path('grn-detail/<int:pk>/', views.GrnDetailDetail.as_view(), name='grn-detail-detail'),
    path('grn-detail/create/', views.GrnDetailCreate.as_view(), name='grn-detail-create'),
    path('grn-detail/update/<int:pk>/', views.GrnDetailUpdate.as_view(), name='grn-detail-update'),
    path('grn-detail/delete/<int:pk>/', views.GrnDetailDelete.as_view(), name='grn-detail-delete'),
]