import csv

from django.core.management import BaseCommand

from app.models import Driver





class Command(BaseCommand):
    help: str = "Import data from csv files with management command"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        path = options.get("path")

        with open(file=path, mode="r") as f:

            csv_file = csv.reader(f, dialect="excel")
            column_names: list = next(csv_file)

            for row in csv_file:
                print(f"row = {row}")

