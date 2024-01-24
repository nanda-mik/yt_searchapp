from typing import Any
from django.core import management

from searchapp import models


class Command(management.base.BaseCommand):
    """
    Check and load fixture for the required tables.
    """

    def load_fixture(self, model_klass, fixture_name, database):
        try:
            if not model_klass.objects.exists():
                management.call_command("loaddata", fixture_name, verbosity=0, database=database)
                self.stdout.write(self.style.SUCCESS(f"Successfully applied fixture :: {fixture_name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Data already present for fixture :: {fixture_name}"))
        except Exception as exc:
            self.stdout.write(self.style.ERROR(f'Failed to apply {fixture_name} fixture due to err : {exc}'))

    def handle(self, *args: Any, **options: Any):
        """
        overrid handle to load fixture.
        """
        db = options.get('database', 'default')
        self.load_fixture(models.LastPushDatetime, "lastpushdatetime", db)
