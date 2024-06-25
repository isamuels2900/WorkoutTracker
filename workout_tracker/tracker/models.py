from django.db import models
from django.contrib.auth.models import User

    
#Class for each exercise 
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
#Class for each template
class Template(models.Model):
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through='TemplateExercise')
    
    def __str__(self):
        return self.name
    

class TemplateExercise(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    
    class Meta:
        unique_together = ('template','exercise')