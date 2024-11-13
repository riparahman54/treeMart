from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request):
    return HttpResponse("<h1>Welcome to login page</h1>")