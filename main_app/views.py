from django.shortcuts import render
from django.http import HttpResponse

class Show:
  def __init__(self, title, season, year, description):
    self.title = title
    self.season = season
    self.year = year
    self.description = description

shows = [
  Show('Squid Game', 1, 2022, 'Play games to survive'),
  Show('Stranger Things', 4, 2022, 'Back to the dark world'),
  Show('Alice in Borderland', 1, 2020, 'Enter the game world')
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def shows_index(request):
  return render(request, 'shows/index.html', { 'shows': shows })
