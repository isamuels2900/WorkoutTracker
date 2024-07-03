from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Mixins for create and update verification
from tracker.models import Template, Exercise, TemplateExercise
from .forms import one_rep_max_calculator_form # Imports the form to calculate one rep maxes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'tracker/home.html')

class TemplateListView(ListView):
    model = Template # The model to query for the list view
    template_name = 'tracker/home.html' # template ListView uses
    context_object_name = 'object_list'
    
    ##### This is supposed to order by latest but it is not really working ###
    def get_queryset(self):
        return Template.objects.all().order_by('-last_updated')
    
    # We override the get_context_data method to add multiple context object names
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['templates'] = Template.objects.filter(author = 1)
        context['exercises'] = Exercise.objects.all()
        context['template_exercise'] = TemplateExercise.objects.all()
        return context
    
# Detailed template view only shows the template information not the exercises or templateExercise info
class TemplateDetailView(DetailView):
    model = Template # The model to query for the list view
    template_name = 'tracker/template_detail.html' # template ListView uses
    context_object_name = 'template'
    
    # We override the get_context_data method to add multiple context object names
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_exercises'] = Exercise.objects.all()
        context['template_exercise'] = TemplateExercise.objects.filter(template=self.object)
        context['exercises'] = self.object.exercises.all()
        return context
    
class TemplateCreateView(LoginRequiredMixin, CreateView):
    model = Template
    fields = ['name']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TemplateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Template
    fields = ['name']
    
    # Checks if form data is valid 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Checks if template author is the one trying to update a template
    def test_func(self):
        template = self.get_object()
        if self.request.user == template.author:
            return True
        return False

class TemplateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Template
    success_url = '/my_workouts'
    
    # Checks if template author is the one trying to update a template
    def test_func(self):
        template = self.get_object()
        if self.request.user == template.author:
            return True
        return False

def about(request):
    return render(request, 'tracker/about.html', { 'title':'about'})

def one_rep_max_calc(request):  
    if request.method == 'POST':
        form = one_rep_max_calculator_form(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            reps = form.cleaned_data['reps']
            # Epley formula for 1RM calculation
            one_rep_max = weight * (1 + reps / 30)
            # Round to 2 decimal places
            one_rep_max = round(one_rep_max, 1)
            
            # Percentages based on the one rep max to display on the 1rm calculator html 
            one_rep_max95 = one_rep_max * 0.95
            one_rep_max95 = round(one_rep_max95, 1)
            
            one_rep_max90 = one_rep_max * 0.90
            one_rep_max90 = round(one_rep_max90, 1)
            
            one_rep_max85 = one_rep_max * 0.85
            one_rep_max85 = round(one_rep_max85, 1)
            
            one_rep_max80 = one_rep_max * 0.80
            one_rep_max80 = round(one_rep_max80, 1)
            
            one_rep_max75 = one_rep_max * 0.75
            one_rep_max75 = round(one_rep_max75, 1)
            
            one_rep_max70 = one_rep_max * 0.70
            one_rep_max70 = round(one_rep_max70, 1)
            
            one_rep_max65 = one_rep_max * 0.65
            one_rep_max65 = round(one_rep_max65, 1)
            
            one_rep_max60 = one_rep_max * 0.60
            one_rep_max60 = round(one_rep_max60, 1)
            
            one_rep_max55 = one_rep_max * 0.55
            one_rep_max55 = round(one_rep_max55, 1)
            
            one_rep_max50 = one_rep_max * 0.50
            one_rep_max50 = round(one_rep_max50, 1)
            
            return render(request, 'tracker/one_rep_max_calculator.html', 
                          {'form':form, 
                           'one_rep_max':one_rep_max,
                           'one_rep_max95':one_rep_max95,
                           'one_rep_max90':one_rep_max90,
                           'one_rep_max85':one_rep_max85,
                           'one_rep_max80':one_rep_max80,
                           'one_rep_max75':one_rep_max75,
                           'one_rep_max70':one_rep_max70,
                           'one_rep_max65':one_rep_max65,
                           'one_rep_max60':one_rep_max60,
                           'one_rep_max55':one_rep_max55,
                           'one_rep_max50':one_rep_max50,})
    else:
        form = one_rep_max_calculator_form()
    return render(request, 'tracker/one_rep_max_calculator.html', {'form':form})

def view_exercises(request):
    context = {
        'exercises': Exercise.objects.all()
    }
    return render(request, 'tracker/exercises.html',context)
