from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/', include('plants.urls')),
    path('api/', include('varieties.urls')),
    path('api/', include('branches.urls')),
    path('api/', include('customers.urls')),
    path('api/', include('lands.urls')),
    path('api/', include('lands_plants.urls')),
    path('api/', include('stocks.urls')),
]
