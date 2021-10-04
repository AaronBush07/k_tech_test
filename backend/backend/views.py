from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import colours
import json


@csrf_exempt
def colour_picker(request):
    if request.method == 'GET': 
        #Generate random colours
        new_colours = []
        for i in range(0,5): 
            colour = colours.random_colour()
            new_colours.append(colour.props())
        return HttpResponse(json.dumps(new_colours), status=200)
    else: 
        return HttpResponse(status=404)



