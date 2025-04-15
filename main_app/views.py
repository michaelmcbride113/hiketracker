
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hike
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'

class HikeCreate(LoginRequiredMixin, CreateView):
    model = Hike
    fields = ['name', 'location', 'difficulty', 'date', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HikeUpdate(LoginRequiredMixin, UpdateView):
    model = Hike
    fields = ['name', 'location', 'difficulty', 'date', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HikeDelete(LoginRequiredMixin, DeleteView):
    model = Hike
    success_url = '/hikes/'
    def get_queryset(self):
        return Hike.objects.filter(user=self.request.user)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hike-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def hike_index(request):
    hikes = Hike.objects.filter(user=request.user)
    return render(request, 'hikes/index.html', {'hikes': hikes})

@login_required
def hike_detail(request, hike_id):
    hike = Hike.objects.get(id=hike_id)
    return render(request, 'hikes/detail.html', {'hike': hike})