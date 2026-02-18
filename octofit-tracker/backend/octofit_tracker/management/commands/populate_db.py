from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Teams
        marvel = Team.objects.create(name="Marvel", description="Marvel heroes")
        dc = Team.objects.create(name="DC", description="DC heroes")

        # Users
        batman = User.objects.create(email="batman@dc.com", username="Batman", team_id=str(dc.id))
        spiderman = User.objects.create(email="spiderman@marvel.com", username="Spiderman", team_id=str(marvel.id))
        wonderwoman = User.objects.create(email="wonderwoman@dc.com", username="Wonder Woman", team_id=str(dc.id))

        # Activities
        Activity.objects.create(user_id=str(spiderman.id), type="Running", duration=30, date=timezone.now().date())
        Activity.objects.create(user_id=str(batman.id), type="Cycling", duration=45, date=timezone.now().date())

        # Workouts
        strength = Workout.objects.create(name="Strength", description="Strength training", suggested_for_ids=[str(wonderwoman.id)])

        # Leaderboard
        Leaderboard.objects.create(team_id=str(marvel.id), points=100)
        Leaderboard.objects.create(team_id=str(dc.id), points=80)

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
