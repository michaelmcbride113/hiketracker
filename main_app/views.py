
from django.shortcuts import render
from .models import Hike

# class Hike:
#     def __init__(self, name, location, difficulty, date, description):
#         self.name = name
#         self.location = location
#         self.difficulty = difficulty
#         self.date = date
#         self.description = description

# hikes = [
#     Hike('Mt. Beacon', 'Beacon, NY', 'Medium', '4/5/2025', 'Fun hike, tough at the beginning but gets easier'),
#     Hike('Breakneck Ridge', 'Cold Spring, NY', 'Medium', '4/6/2025', 'Fun hike, lots of scrambling'),
#     Hike('Lake Minewaska', 'New Paltz, NY', 'Easy', '4/7/2025', 'Easy loop trail around a lake')
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hike_index(request):
    hikes = Hike.objects.all()
    return render(request, 'hikes/index.html', {'hikes': hikes})

def hike_detail(request, hike_id):
    hike = Hike.objects.get(id=hike_id)
    return render(request, 'hikes/detail.html', {'hike': hike})