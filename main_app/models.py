from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

RATINGS = (
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5)
)

# Create your models here.
class Performer(models.Model):
  name = models.CharField(max_length=50)
  born_year = models.IntegerField()

  def __str__(self):
    return f"{self.name}, born in {self.born_year}"

  def get_absolute_url(self):
    return reverse('performers_detail', kwargs={'pk': self.id})

class Show(models.Model):
  title = models.CharField(max_length=100)
  season = models.IntegerField()
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  performers = models.ManyToManyField(Performer)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'show_id': self.id})


class Review(models.Model):
  rating = models.IntegerField(
    choices=RATINGS,
    default=RATINGS[4][0]
  )
  comment = models.TextField(max_length=250)

  show = models.ForeignKey(Show, on_delete=models.CASCADE)

  def __str__(self):
    return f"Rating is {self.get_rating_display()}, comment: {self.comment}"

  class Meta:
    ordering = ['-rating']