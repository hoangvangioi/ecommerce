from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Run all migrations commands for setup"

    def handle(self, *args, **options):

        commands = [
            "makemigrations",
            "migrate",
            "migrate --database=book_db",
            "migrate --database=category_db",
            "migrate --database=clothes_db",
            "migrate --database=mobile_db",
            "migrate --database=cart_db",
        ]

        for cmd in commands:
            try:
                call_command(*cmd.split())
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error executing command: {cmd}"))
                self.stdout.write(self.style.ERROR(str(e)))