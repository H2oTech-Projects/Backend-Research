from django.http import JsonResponse

def author_list(request):
    return JsonResponse({"message": "List of authors"})
