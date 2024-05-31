from django.shortcuts import render, HttpResponse

## for testing purpose
def new(request):
    return HttpResponse('this is new route')
