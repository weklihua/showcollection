from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('shows/', views.shows_index, name='index'),
  path('shows/<int:show_id>/', views.shows_detail, name='detail'),
  path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
  path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
  path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
  path('shows/<int:show_id>/add_review/', views.add_review, name='add_review'),
  path('shows/<int:show_id>/assoc_performer/<int:performer_id>/', views.assoc_performer, name='assoc_performer'),

  path('performers/', views.PerformerList.as_view(), name='performers_index'),
  path('performers/<int:pk>/', views.PerformerDetail.as_view(), name='performers_detail'),
  path('performers/create/', views.PerformerCreate.as_view(), name='performers_create'),
  path('performers/<int:pk>/update/', views.PerformerUpdate.as_view(), name='performers_update'),
  path('performers/<int:pk>/delete/', views.PerformerDelete.as_view(), name='performers_delete'),
]
