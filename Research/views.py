from django.http import JsonResponse
from rest_framework.views import APIView
from .utils import upload_geotiff
import os
import tempfile

class UploadTIFFView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        print(request.FILES)  # Should show the uploaded file

        if not file:
            return JsonResponse({"error": "No file provided"}, status=400)
        
        workspace = request.POST.get('workspace')
        print(workspace)
        store_name = os.path.splitext(file.name)[0]
        print(store_name)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.tif') as temp_file:
            file_path = temp_file.name
            for chunk in file.chunks():
                temp_file.write(chunk)
        
        try:
            # Upload to GeoServer
            result = upload_geotiff(workspace, store_name, file_path)
        except Exception as e:
            os.remove(file_path)  # Clean up the temporary file
            return JsonResponse({"error": str(e)}, status=500)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        return JsonResponse({"message": result})
