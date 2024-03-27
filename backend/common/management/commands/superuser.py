from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **options):
        User.objects.create_superuser(
            username='admin',
            first_name='FirstName',
            last_name='LastName',
            email='admin@admin.com',
            password='1',
        )
        print("Created superuser!")
