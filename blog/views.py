from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello Everyone Welcome to my Blogging Page")