from django.shortcuts import render
from .models import Show

# class Show:
#   def __init__(self, title, season, year, description):
#     self.title = title
#     self.season = season
#     self.year = year
#     self.description = description

# shows = [
#   Show('Squid Game', 1, 2022, 'Play games to survive'),
#   Show('Stranger Things', 4, 2022, 'Back to the dark world'),
#   Show('Alice in Borderland', 1, 2020, 'Enter the game world')
# ]


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