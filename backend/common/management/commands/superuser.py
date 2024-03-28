from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings



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
