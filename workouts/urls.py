from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.login_page , name='login'),
    path('register/' , views.register , name='register'),
    path('logout/' , views.logout_user , name='logout'),
    path('dashboard' , views.dashboard , name='dashboard'),
    path('workout/add/' , views.add_workout , name='add_workout'),
    path('workout/<int:workout_id>/add-entries/' , views.add_entries , name='add_entries'),
    path('history/' , views.workout_history, name='workout_history'),
    path('workout/delete/<int:workout_id>/' ,  views.delete_workout , name='delete_workout'),
    path('about/' , views.about , name='about'),
    path('workout/edit/<int:workout_id>' , views.edit_workout , name='edit_workout'),
    path('api/workouts/' , views.api_workout , name='api_workout'),
    path('send-summary/', views.send_summary, name='send_summary'),


    
]