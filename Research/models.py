from django.db import models

class GeoTIFFUpload(models.Model):
    file = models.FileField(upload_to='geotiff_files/')
    workspace = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
