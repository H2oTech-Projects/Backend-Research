from django.contrib import admin
from .models import GeoTIFFUpload

@admin.register(GeoTIFFUpload)
class GeoTIFFUploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'workspace', 'store_name', 'uploaded_at')