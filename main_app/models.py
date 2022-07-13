from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse


# Create your models here.

class Show(models.Model):
  title = models.CharField(max_length=100)
  season = models.IntegerField()
  year = models.IntegerField()
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'show_id': self.id})



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