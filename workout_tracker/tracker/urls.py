from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tracker-home'),
    path('about/', views.about, name='tracker-about'),
    path('one_rep_max_calculator/', views.one_rep_max_calc, name='tracker-one_rep_max_calc'),
    path('exercises/', views.view_exercises, name='tracker-exercises'),
]
