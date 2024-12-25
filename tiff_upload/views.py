from django.http import JsonResponse
from django.views import View
from requests.auth import HTTPBasicAuth
import requests

class UploadGeoTIFFView(View):
    def post(self, request):
        username = "admin"
        password = "geoserver"
        geoserver_url = "http://localhost:8080/geoserver"
        workspace = "workspace2"
        store_name = request.POST.get("store_name")
        tif_file_path = "file:///D:/Downloads/HYP_50M_SR_W.tif"
        crs = "EPSG:4326"
        style_name = "NDVI"

        # REST API URLs
        store_url = f"{geoserver_url}/rest/workspaces/{workspace}/coveragestores"
        layer_url = f"{geoserver_url}/rest/workspaces/{workspace}/coveragestores/{store_name}/coverages"
        style_url = f"{geoserver_url}/rest/layers/{store_name}.xml"

        # Auth
        auth = HTTPBasicAuth(username, password)

        # Payloads
        store_payload = {
            "coverageStore": {
                "name": store_name,
                "type": "GeoTIFF",
                "workspace": workspace,
                "enabled": True,
                "url": tif_file_path,
            }
        }

        layer_payload = {
            "coverage": {
                "name": store_name,  # Layer name matches store name
                "srs": crs,
                "title": store_name,
                "enabled": True,
            }
        }

        style_payload = f"""
        <layer>
            <defaultStyle>
                <name>{style_name}</name>
            </defaultStyle>
        </layer>
        """

        try:
            # Authenticate
            if requests.get(geoserver_url, auth=auth).status_code != 200:
                return JsonResponse({"error": "Authentication failed. Check your credentials."}, status=401)

            # Create GeoTIFF Store
            store_response = requests.post(store_url, json=store_payload, auth=auth)
            if store_response.status_code == 201:
                # Create Layer
                layer_response = requests.post(layer_url, json=layer_payload, auth=auth)
                if layer_response.status_code == 201:
                    # Assign Style to Layer
                    headers = {"Content-type": "application/xml"}
                    style_response = requests.put(style_url, data=style_payload, headers=headers, auth=auth)
                    if style_response.status_code == 200:
                        return JsonResponse({"message": "Layer and style created successfully!"})
                    return JsonResponse({"error": "Error updating layer style."}, status=500)
                return JsonResponse({"error": "Error creating layer."}, status=500)
            return JsonResponse({"error": "Error creating store.", "details": store_response.text}, status=500)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
