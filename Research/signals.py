#You can use the post_save signal to trigger the Celery task whenever a file is saved.

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GeoTIFFUpload
from .tasks import upload_file_to_geoserver
import os

@receiver(post_save, sender=GeoTIFFUpload)
def trigger_upload_to_geoserver(sender, instance, created, **kwargs):
    if created:
        file_path = instance.file.path
        if os.path.exists(file_path):
            print(f"File {instance.file.name} saved, triggering upload...")
            upload_file_to_geoserver.delay(file_path, instance.workspace, instance.store_name)
        else:
            print(f"Error: File {instance.file.name} does not exist.")