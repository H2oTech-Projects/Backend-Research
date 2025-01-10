import requests
import os

GEOSERVER_URL = "http://staging.flowgeos.wateraccounts.com/geoserver/"
USERNAME = "admin"
PASSWORD = "rGcBq0kq}]75"

def upload_geotiff(workspace, store_name, file_path):
    content_type = "image/tiff" if file_path.endswith(".tif") else "application/zip"

    url = f"{GEOSERVER_URL}/rest/workspaces/{workspace}/coveragestores/{store_name}/file.geotiff"
    headers = {"Content-Type": content_type}
    
    with open(file_path, "rb") as file:
        response = requests.put(
            url,
            auth=(USERNAME, PASSWORD),
            headers=headers,
            data=file
        )
    
    if response.status_code in [201, 202]:
        return f"Successfully uploaded {os.path.basename(file_path)}."
    else:
        raise Exception(
            f"Failed to upload {os.path.basename(file_path)}: {response.status_code} {response.text}"
        )