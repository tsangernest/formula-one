import csv

from django.core.management import BaseCommand, CommandError

from app.models import Driver


class Command(BaseCommand):
    help: str = "Import data from csv files with management command"

    def add_arguments(self, parser):
        parser.add_argument(action="--path", type=str)

    def handle(self, *args, **options):
        path: str = options["path"]
        with open(file=path, mode="rt") as csv_file:
            reader = csv.reader(csvfile=csv_file, dialect="excel")
            for row in reader:
                print(f"row = {row}")


