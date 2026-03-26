from django.contrib import admin
from .models import Workout, WorkoutEntry , CoachProgram

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date', 'user']
    list_filter = ['category']
    search_fields = ['name', 'user__username']

@admin.register(WorkoutEntry)
class WorkoutEntryAdmin(admin.ModelAdmin):
    list_display = ['exercise_name', 'sets', 'reps', 'weight_kg', 'workout']


@admin.register(CoachProgram)
class CoachProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title']


