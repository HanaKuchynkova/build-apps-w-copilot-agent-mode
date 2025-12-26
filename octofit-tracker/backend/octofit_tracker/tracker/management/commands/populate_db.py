from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio endurance', difficulty='Medium'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], workout=workouts[0], date=timezone.now(), duration_minutes=30, points=50)
        Activity.objects.create(user=users[1], workout=workouts[1], date=timezone.now(), duration_minutes=45, points=70)
        Activity.objects.create(user=users[2], workout=workouts[0], date=timezone.now(), duration_minutes=20, points=30)
        Activity.objects.create(user=users[3], workout=workouts[1], date=timezone.now(), duration_minutes=60, points=90)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=120)
        Leaderboard.objects.create(team=dc, total_points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
