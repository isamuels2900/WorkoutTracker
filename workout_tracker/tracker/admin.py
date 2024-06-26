from django.contrib import admin
from tracker.models import Exercise, TemplateExercise, Template, Muscle, Category

admin.site.register(Muscle)
admin.site.register(Category)
admin.site.register(Exercise)
admin.site.register(Template)
admin.site.register(TemplateExercise)