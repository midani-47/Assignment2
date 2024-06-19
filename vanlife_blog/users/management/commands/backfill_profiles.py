from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

User = get_user_model()

class Command(BaseCommand):
    help = 'Backfill profiles for users that do not have one'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            Profile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS(f'Backfilled profiles for {users_without_profiles.count()} users'))
