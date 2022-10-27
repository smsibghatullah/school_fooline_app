from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fetch and insert students in db'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("Command Started At %s" % time)



        time = timezone.now().strftime('%X')
        self.stdout.write("Command Ended At %s" % time)