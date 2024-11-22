from django.shortcuts import render

from trees.models import Tree


# Create your views here.
def plant_guide(request):
    return render(request, 'select_season.html')


def select_season(request):
    # Display a form or page for selecting a season
    return render(request, 'select_season.html')


def plants_by_season(request, season):
    # Fetch trees (plants) suitable for the selected season
    trees = Tree.objects.filter(season=season)

    # Pass the trees and the selected season to the template
    return render(request, 'plants_by_season.html', {'trees': trees, 'season': season})