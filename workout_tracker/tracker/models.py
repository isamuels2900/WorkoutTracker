from django.db import models
from django.contrib.auth.models import User

    
class Muscle(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['muscle']
    
    def __str__(self):
        return self.name
    
class Template(models.Model):
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through='TemplateExercise')
    
    class Meta:
        ordering = ['last_updated']
        
    def __str__(self):
        return self.name

class TemplateExercise(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    
    class Meta:
        unique_together = ('template','exercise')