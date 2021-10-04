from django.http import HttpResponse

def colour_picker(request):
    if request.method == 'GET': 
        return HttpResponse('OK', status=200)
    else: 
        return HttpResponse(status=404)



