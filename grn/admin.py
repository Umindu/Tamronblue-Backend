from django.contrib import admin
from .models import Grn, GrnDetail

# Register your models here.
admin.site.register(GrnDetail)
admin.site.register(Grn)