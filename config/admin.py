from django.contrib import admin
from .models import APIKey

# Register your models here.
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'created_at', 'updated_at')
    search_fields = ('name', 'key')
    readonly_fields = ('created_at', 'updated_at')

# Registration
admin.site.register(APIKey, APIKeyAdmin)