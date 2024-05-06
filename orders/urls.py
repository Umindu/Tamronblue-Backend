from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('order/create/', views.OrderCreate.as_view(), name='order-create'),
    path('order/update/<int:pk>/', views.OrderUpdate.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', views.OrderDelete.as_view(), name='order-delete'),

    path('orderitems/', views.OrderItemList.as_view(), name='orderitem-list'),
    path('orderitem/<int:pk>/', views.OrderItemDetail.as_view(), name='orderitem-detail'),
    path('orderitem/create/', views.OrderItemCreate.as_view(), name='orderitem-create'),
    path('orderitem/update/<int:pk>/', views.OrderItemUpdate.as_view(), name='orderitem-update'),
    path('orderitem/delete/<int:pk>/', views.OrderItemDelete.as_view(), name='orderitem-delete'),

    path('payments/', views.PaymentList.as_view(), name='payment-list'),
    path('payment/<int:pk>/', views.PaymentDetail.as_view(), name='payment-detail'),
    path('payment/create/', views.PaymentCreate.as_view(), name='payment-create'),
    path('payment/update/<int:pk>/', views.PaymentUpdate.as_view(), name='payment-update'),
    path('payment/delete/<int:pk>/', views.PaymentDelete.as_view(), name='payment-delete'),
]