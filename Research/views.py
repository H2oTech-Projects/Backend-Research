from django.http import JsonResponse
from rest_framework.views import APIView
from .utils import upload_geotiff
import os
import tempfile
import zipfile
# to upload single file
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

#to upload multiple files
'''
class UploadTIFFView(APIView):
    def post(self, request):
        files = request.FILES.getlist('file')  # Ensure this key matches your Postman request
        if not files:
            return JsonResponse({"error": "No files provided"}, status=400)

        workspace = request.POST.get('workspace')
        if not workspace:
            return JsonResponse({"error": "Workspace is required"}, status=400)

        responses = []
        for file in files:
            if not file.name.endswith(('.tiff', '.tif')):
                responses.append({"file": file.name, "error": "Invalid file type. Only GeoTIFF files are allowed."})
                continue

            store_name = os.path.splitext(file.name)[0]  # Create store name from file name
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.tiff') as temp_file:
                    for chunk in file.chunks():
                        temp_file.write(chunk)
                    file_path = temp_file.name

                # Upload to GeoServer
                result = upload_geotiff(workspace, store_name, file_path)
                responses.append({"file": file.name, "message": result})
            except Exception as e:
                responses.append({"file": file.name, "error": str(e)})
            finally:
                # Clean up the temporary file
                if os.path.exists(file_path):
                    os.remove(file_path)

        return JsonResponse({"results": responses})
'''
'''
class UploadTIFFView(APIView):
    def post(self, request):
        files = request.FILES.getlist('file')  # Ensure this key matches your Postman request
        if not files:
            return JsonResponse({"error": "No files provided"}, status=400)

        workspace = request.POST.get('workspace')
        if not workspace:
            return JsonResponse({"error": "Workspace is required"}, status=400)

        responses = []
        for file in files:
            if file.name.endswith('.zip'):  # Check if the file is a ZIP file
                try:
                    # Create a temporary directory to extract the ZIP contents
                    with tempfile.TemporaryDirectory() as temp_dir:
                        with zipfile.ZipFile(file, 'r') as zip_ref:
                            zip_ref.extractall(temp_dir)

                        # Now process all TIFF files in the extracted directory
                        for extracted_file in os.listdir(temp_dir):
                            if extracted_file.endswith(('.tiff', '.tif')):
                                file_path = os.path.join(temp_dir, extracted_file)
                                store_name = os.path.splitext(extracted_file)[0]  # Store name from the extracted file
                                
                                # Upload the GeoTIFF to GeoServer
                                result = upload_geotiff(workspace, store_name, file_path)
                                responses.append({"file": extracted_file, "message": result})
                            else:
                                responses.append({"file": extracted_file, "error": "Invalid file type. Only GeoTIFF files are allowed."})
                except Exception as e:
                    responses.append({"file": file.name, "error": str(e)})

            elif file.name.endswith(('.tiff', '.tif')):  # Directly handle GeoTIFF files
                try:
                    # Write the file to a temporary location
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.tiff') as temp_file:
                        for chunk in file.chunks():
                            temp_file.write(chunk)
                        file_path = temp_file.name

                    # Upload to GeoServer
                    store_name = os.path.splitext(file.name)[0]  # Create store name from file name
                    result = upload_geotiff(workspace, store_name, file_path)
                    responses.append({"file": file.name, "message": result})
                except Exception as e:
                    responses.append({"file": file.name, "error": str(e)})
                finally:
                    # Clean up the temporary file
                    if os.path.exists(file_path):
                        os.remove(file_path)

        return JsonResponse({"results": responses})


'''