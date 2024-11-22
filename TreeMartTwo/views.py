from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def plant_guide(request):
    return render(request, 'plants_by_season.html')
