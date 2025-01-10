from celery import shared_task
from .utils import upload_geotiff

@shared_task
def upload_file_to_geoserver(file_path, workspace, store_name):
    print(f"Uploading file: {file_path}, to workspace: {workspace}, store: {store_name}")
    try:
        upload_geotiff(workspace, store_name, file_path)
    except Exception as e:
        print(f"Error uploading file: {e}")
        