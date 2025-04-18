from django.shortcuts import render

from trees.models import Tree
import requests

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






def weather_check(request):
    weather_data = None
    tree_recommendation = None

    if request.method == "POST":
        city = request.POST.get('city')
        api_key = '81f59dee117443268c250122251804'
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and 'error' not in data:
            weather_data = {
                'city': data['location']['name'],
                'region': data['location']['region'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon'],
            }

            # tree recommendation
            tree_recommendation = recommend_tree(data['current']['condition']['text'])
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather.html', {
        'weather': weather_data,
        'tree': tree_recommendation
    })


def recommend_tree(condition):
    condition = condition.lower()
    if 'rain' in condition or 'storm' in condition:
        return "Coconut Tree 🌴 (suitable for humid and coastal areas)"
    elif 'clear' in condition or 'sunny' in condition:
        return "Neem Tree 🌳 (great for sunny, dry climates)"
    elif 'Partly Cloudy' in condition:
        return "Mango Tree 🥭 (good in mild cloudy weather)"
    elif 'snow' in condition:
        return "Pine Tree 🌲 (ideal for cold, snowy climates)"
    else:
        return "Banyan Tree 🌳 (suitable for most weather types)"
