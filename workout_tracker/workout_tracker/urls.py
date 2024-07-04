"""
URL configuration for workout_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views # Imports views for user authentication (login, etc..)
from django.urls import path, include
from users import views as user_views # Imports views from users app
from users.views import WorkoutsListView # Imports the List View for my workouts
# Imports settings for media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('my_workouts/', WorkoutsListView.as_view(), name='users-my_workouts'),
    path('add_exercises/', user_views.addExercises, name='users-add_exercises'),
    
    # Password reset 
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
             ), 
         name='password_reset'),
    
    #Password reset done
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
            ), 
        name='password_reset_done'),
    
    # Password reset confirm
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
             ), 
         name='password_reset_confirm'),
    
    # Password reset complete
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
             ), 
         name='password_reset_complete'),
    
    path('', include('tracker.urls')),
]

# This allows our media to work in the browser
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
