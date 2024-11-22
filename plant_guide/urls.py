from django.urls import path
from . import views

urlpatterns = [


    path('plant-guide/', views.plant_guide, name='plant_guide'),

    path('select-season/', views.select_season, name='select_season'),
    path('plants-by-season/<season>/', views.plants_by_season, name='plants_by_season'),

]