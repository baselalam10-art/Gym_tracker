from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Workout , WorkoutEntry
from django.http import JsonResponse

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    total_workouts = workouts.count()
    latest_workout = workouts.first()

    context = {
        'total_workouts':total_workouts,
        'latest_workout':latest_workout,
    }
    return render(request, 'dashboard.html' , context)


def add_workout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        date = request.POST['date']
        notes = request.POST.get('notes', '')

        if not name or not category or not date:
            messages.error(request, 'Please fill in all required fields')
            return redirect('add_workout')

        workout = Workout.objects.create(
            user=request.user,
            name=name,
            category=category,
            date=date,
            notes=notes
        )
        return redirect('add_entries', workout_id=workout.id)

    return render(request, 'add_workout.html')


def add_entries(request, workout_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    workout = Workout.objects.get(id=workout_id)
    
    if request.method == 'POST':
        exercise_name = request.POST['exercise_name']
        sets = request.POST['sets']
        reps = request.POST['reps']
        weight_kg = request.POST['weight_kg']

        if not exercise_name or not sets or not reps or not weight_kg:
            messages.error(request, 'Please fill in all fields')
            return redirect('add_entries', workout_id=workout_id)

        WorkoutEntry.objects.create(
            workout=workout,
            exercise_name=exercise_name,
            sets=sets,
            reps=reps,
            weight_kg=weight_kg
        )
        return redirect('add_entries', workout_id=workout_id)

    entries = WorkoutEntry.objects.filter(workout=workout)
    context = {
        'workout': workout,
        'entries': entries
    }
    return render(request, 'add_entries.html', context)


def workout_history(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    category_filter = request.GET.get('category', '')
    
    if category_filter:
        workouts = workouts.filter(category=category_filter)

    categories = Workout.objects.filter(user=request.user).values_list('category', flat=True).distinct()

    context = {
        'workouts': workouts,
        'categories': categories,
        'selected_category': category_filter,
    }
    return render(request, 'workout_history.html', context)

def delete_workout(request, workout_id):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        workout = Workout.objects.get(id=workout_id, user=request.user)
        workout.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def about(request):
    return render(request , 'about.html')


def edit_workout(request , workout_id):
    if not request.user.is_authenticated:
        return redirect('login')
    workout = Workout.objects.get(id=workout_id , user=request.user)

    if request.method == 'POST':
        workout.name = request.POST['name']
        workout.category=request.POST['category']
        workout.date=request.POST['date']
        workout.notes=request.POST['notes']
        workout.save()
        return redirect('workout_history')
    return render(request , 'edit_workout.html' , {'workout':workout})

def api_workout(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error' : 'Unauthorized'} , status=401)
    
    all_workouts = Workout.objects.filter(user=request.user).order_by('-date')
    data = []
    for workout in all_workouts:
        data.append({
            'id':workout.id,
            'name':workout.name,
            'category':workout.category,
            'date':str(workout.date),
            'notes':workout.notes,
            'total_exercises': workout.entries.count()
        })

    return JsonResponse({
         'total_workouts': all_workouts.count(),
         'workouts': data
     })    


