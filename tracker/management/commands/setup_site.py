from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'Create default site'

    def handle(self, *args, **options):
        site, created = Site.objects.get_or_create(
            domain='127.0.0.1:8000',
            defaults={'name': 'localhost'}
        )
        if created:
            self.stdout.write(f'Created site: {site}')
        else:
            self.stdout.write(f'Site already exists: {site}')