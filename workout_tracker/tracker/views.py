from django.shortcuts import render
from django.http import HttpResponse
from tracker.models import Template, Exercise, TemplateExercise

def home(request):
    context = {
        'templates': Template.objects.all(),
        'exercises': Exercise.objects.all(),
        'template_exercise': TemplateExercise.objects.all(),
    }
    return render(request, 'tracker/home.html', context)

def about(request):
    return render(request, 'tracker/about.html', { 'title':'about'})