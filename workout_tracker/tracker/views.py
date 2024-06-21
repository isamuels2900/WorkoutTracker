from django.shortcuts import render
from django.http import HttpResponse

templates = [
    {
        'author': 'samuelsian',
        'title': 'Push Day',
        'exercises': ['Bench Press 5x5', 'Overhead Press 3x10', 'Tricep Dips 3x15'],
        'date_posted': 'June 16,2024'
    },
    {
        'author': 'samuelsian',
        'title': 'Pull Day',
        'exercises': ['Deadlift 5x5', 'Pull Ups 3x10', 'Bicep Curl 3x15'],
        'date_posted': 'June 12,2024'
    }
]

def home(request):
    context = {
        'templates': templates
    }
    return render(request, 'tracker/home.html', context)

def about(request):
    return render(request, 'tracker/about.html', { 'title':'about'})