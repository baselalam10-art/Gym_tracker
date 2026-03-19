# 🏋️ Gym Workout Tracker

A full-stack web application built with Django and MySQL that helps users log, track, and manage their gym workout sessions.

---

## 🚀 Live Demo
> Coming soon (AWS Deployment)

---

## 📋 Features

- ✅ User Registration & Login with secure authentication
- ✅ Create and log workout sessions
- ✅ Add exercises with sets, reps, and weight
- ✅ View full workout history with category filtering
- ✅ Edit and delete workouts
- ✅ Dashboard with charts and activity summary
- ✅ AJAX integration for smooth interactions
- ✅ REST API endpoint for workout data
- ✅ Fully responsive design (Bootstrap 5)

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Django 6 | Backend framework |
| Python 3 | Programming language |
| MySQL | Database |
| Bootstrap 5 | Frontend styling |
| Chart.js | Dashboard charts |
| JavaScript | AJAX & interactivity |
| AWS | Deployment |
| Git & GitHub | Version control |

---

## 🗄️ Database Schema

3 Tables:
- *User* — Django's built-in user model
- *Workout* — Workout sessions linked to a user
- *WorkoutEntry* — Individual exercises linked to a workout

---

## ⚙️ How to Run Locally

1. *Clone the repository*
```bash
git clone https://github.com/baselalam10-art/Gym_tracker.git
cd Gym_tracker

2. Create and activate virtual enviromnent
python -m venv env
env/Scripts/activate

3 install dependencies
pip install django mysqlclient

4.Create MySQL database
CREATE database gym_tracker_db;

5.update settings,py with your mysql credentials

6.Run migrations
python manage.py migrate and makemigrations

7.start the server
python manage.py runserver


8. visit https://127.0.0.1:8000

Developer
Basel-Solo Project | Web Developmnent
Bootcamp | March 2026 