from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Show, Performer
from .forms import ReviewForm


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
  review_form = ReviewForm()
  return render(request, 'shows/detail.html', {
      'show': show, 'review_form': review_form
    })

def add_review(request, show_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.show_id = show_id
    new_review.save()
  return redirect('detail', show_id=show_id)

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

class PerformerList(ListView):
  model = Performer

class PerformerDetail(DetailView):
  model = Performer

class PerformerCreate(CreateView):
  model = Performer
  fields = '__all__'

class PerformerUpdate(UpdateView):
  model = Performer
  fields = ['name', 'born_year']

class PerformerDelete(DeleteView):
  model = Performer
  success_url = '/performers/'