from django.urls import path
from . import views
from .views import TemplateListView, TemplateDetailView

urlpatterns = [
    path('', TemplateListView.as_view(), name='tracker-home'),
    path('template/<int:pk>/', TemplateDetailView.as_view(), name='template-detail'),
    path('about/', views.about, name='tracker-about'),
    path('one_rep_max_calculator/', views.one_rep_max_calc, name='tracker-one_rep_max_calc'),
    path('exercises/', views.view_exercises, name='tracker-exercises'),
]
