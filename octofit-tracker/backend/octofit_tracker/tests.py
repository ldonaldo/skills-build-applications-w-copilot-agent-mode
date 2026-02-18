from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Marvel", description="Marvel heroes")
        self.assertEqual(team.name, "Marvel")

    def test_user_creation(self):
        team = Team.objects.create(name="DC", description="DC heroes")
        user = User.objects.create(email="batman@dc.com", username="Batman", team=team)
        self.assertEqual(user.username, "Batman")

    def test_activity_creation(self):
        team = Team.objects.create(name="Marvel", description="Marvel heroes")
        user = User.objects.create(email="spiderman@marvel.com", username="Spiderman", team=team)
        activity = Activity.objects.create(user=user, type="Running", duration=30, date="2026-02-18")
        self.assertEqual(activity.type, "Running")

    def test_workout_creation(self):
        user = User.objects.create(email="wonderwoman@dc.com", username="Wonder Woman")
        workout = Workout.objects.create(name="Strength", description="Strength training")
        workout.suggested_for.add(user)
        self.assertEqual(workout.name, "Strength")

    def test_leaderboard_creation(self):
        team = Team.objects.create(name="Marvel", description="Marvel heroes")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
