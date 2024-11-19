from django.shortcuts import render
import logging
from django.http import HttpResponse


logger = logging.getLogger('views')

def my_view(request):
    logger.info("Info: my_view was called.")
    logger.debug("Debug: Processing request.")
    logger.warning("Warning: Something might be wrong.")
    logger.error("Error: Something went wrong!")
    return HttpResponse("Logs have been recorded. Check the console and debug.log.")
