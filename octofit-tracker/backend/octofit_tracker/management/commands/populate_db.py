from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with initial data for Octofit Tracker.'

    def handle(self, *args, **options):
        # Teams
        marvel = Team.objects.get_or_create(name="Marvel", description="Marvel heroes")[0]
        dc = Team.objects.get_or_create(name="DC", description="DC heroes")[0]

        # Users
        batman = User.objects.get_or_create(email="batman@dc.com", username="Batman", team=dc)[0]
        spiderman = User.objects.get_or_create(email="spiderman@marvel.com", username="Spiderman", team=marvel)[0]
        wonderwoman = User.objects.get_or_create(email="wonderwoman@dc.com", username="Wonder Woman", team=dc)[0]

        # Activities
        Activity.objects.get_or_create(user=spiderman, type="Running", duration=30, date=timezone.now().date())
        Activity.objects.get_or_create(user=batman, type="Cycling", duration=45, date=timezone.now().date())

        # Workouts
        strength = Workout.objects.get_or_create(name="Strength", description="Strength training")[0]
        strength.suggested_for.add(wonderwoman)

        # Leaderboard
        Leaderboard.objects.get_or_create(team=marvel, points=100)
        Leaderboard.objects.get_or_create(team=dc, points=80)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
