from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELll .world you're at the polls index.")
