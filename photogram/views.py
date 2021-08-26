"""photogram views"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse
#Utilities
from datetime import datetime
from django.http import JsonResponse
import json

from django.shortcuts import render


def hello_world(request):
    """return hello world"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Hi!, Current time server is {now}".format(now=now))

def sort_integers(request):
    """return json with sorted integer"""
    #import pdb; pdb.set_trace()

    numbers = [int(x) for x in request.GET['numbers'].split(",") ]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'ints sorted susccefull.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
 
def say_hi(request, name, age):
    """return hi"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'hello, {} welcome tu photogram'.format(name)
    
    return HttpResponse(message)
