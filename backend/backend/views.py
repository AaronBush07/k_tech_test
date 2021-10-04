from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import colours


@csrf_exempt
def colour_picker(request):
    if request.method == 'GET': 
        #Generate random colours
        print(len(colours.array))
        new_colours = []
        for i in range(0,5): 
            colour = colours.random_colour()
            new_colours.append(colour.props())

        print(new_colours)
        return HttpResponse('OK', status=200)
    else: 
        return HttpResponse(status=404)



