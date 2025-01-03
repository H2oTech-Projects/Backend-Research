from django.http import HttpResponse
import time

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request method: {request.method}, Request URL: {request.get_full_path()}")
        response = self.get_response(request)
        return response
    
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print("Processing request")
        request.start_time = time.time()

    def process_response(self, request, response):
        print("Processing response")
        elapsed_time = time.time() - request.start_time
        response['X-Response-Time'] = str(elapsed_time)
        return response

class ErrorHandlingMiddleware:
    def process_exception(self, request, exception):
        print(f"Exception occurred: {exception}")
        # Optionally, return a custom response
        return HttpResponse("An error occurred", status=500)



