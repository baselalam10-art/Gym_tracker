from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class WorkoutEntry(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='entries')
    exercise_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight_kg = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exercise_name} - {self.workout.name}"
    
    

def build_summary(user):
    workouts = Workout.objects.filter(user=user)
    total_workouts = workouts.count()
    latest_workout = workouts.first()

    entries = latest_workout.entries.all() if latest_workout else []
    exercises = "\n".join([
        f"- {e.exercise_name}: {e.sets}x{e.reps} @ {e.weight_kg}kg"
        for e in entries
    ])

    return f"""
    Hi {user.username},
    Total workouts: {total_workouts}
    Latest workout: {latest_workout.name if latest_workout else 'None'}
    Exercises:
    {exercises if exercises else 'No entries yet'}
    """

class CoachProgram(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    description = models.TextField()
    exercises = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title