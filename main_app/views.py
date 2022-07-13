from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Show

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def shows_index(request):
  shows = Show.objects.all()
  return render(request, 'shows/index.html', { 'shows': shows })

def shows_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show })

class ShowCreate(CreateView):
  model = Show
  fields = '__all__'
  success_url = '/shows/'

class ShowUpdate(UpdateView):
  model = Show
  fields = ['season', 'year', 'description']

class ShowDelete(DeleteView):
  model = Show
  success_url = '/shows/'