from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    read_only_fields = ('created_at', 'updated_at')


admin.site.register(Service, ServiceAdmin)