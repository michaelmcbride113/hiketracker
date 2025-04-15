
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hike

class HikeCreate(CreateView):
    model = Hike
    fields = '__all__'

class HikeUpdate(UpdateView):
    model = Hike
    fields = '__all__'

class HikeDelete(DeleteView):
    model = Hike
    success_url = '/hikes/'

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