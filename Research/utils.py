from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

def custom_exception_handler(exc, context):
  response = exception_handler(exc, context)

  if response is not None:
    response.data['status_code'] = response.status_code
    #response.data['error_code'] = "custom error"
  return response

class ServiceUnavailable(APIException):
    status_code = 503 
    default_detail = 'Service temporarily unavailable, try again later.'  # Error message
    default_code = 'service_unavailable' 