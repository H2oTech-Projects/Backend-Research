from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.http import HttpResponse, Http404

# Get a logger for this module
logger = logging.getLogger('logs.views')

def info_view(request):
    logger.info('Info level log message: info_view called.')
    return HttpResponse("Info level log message logged.")

def debug_view(request):
    logger.debug('Debug level log message: debug_view called.')
    return HttpResponse("Debug level log message logged.")

def warning_view(request):
    logger.warning('Warning level log message: warning_view called.')
    return HttpResponse("Warning level log message logged.")

def error_view(request):
    logger.error('Error level log message: error_view called.')
    return HttpResponse("Error level log message logged.")

def my_view(request):
    try:
        # Simulate some logic that might fail
        if request.GET.get('trigger_error'):
            raise ValueError("Triggered a simulated error!")
        return HttpResponse("All is well!")
    except ValueError as e:
        logger.error(f"ValueError occurred: {e}")
        return HttpResponse("An error occurred, check logs!")
    except Exception as e:
        logger.exception("Unexpected error!")
        raise Http404("Something went wrong!")  # Will also log automatically
    

logger = logging.getLogger('django')

def error_view(request):
    try:
        1 / 0  # Intentional error: division by zero
    except Exception as e:
        logger.error("An error occurred: %s", str(e))  # Log the error
        return HttpResponse("Error logged to error.log")


from django.db import connection

logger = logging.getLogger('django.db.backends')

def my_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM myapp_mymodel WHERE name=%s", ['example'])
        logger.info(f"Query executed: {cursor.query}")
    return HttpResponse("SQL query logged!")
    return HttpResponse('Check console or logs for SQL queries.')