import csv

from django.core.management import BaseCommand

from app.models import Driver


class Command(BaseCommand):
    help: str = "Import data from csv files with management command"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        path = options.get("path")
        print(f"\n{path=}\n")

        with open(file=path, mode="r") as f:

            csv_file = csv.reader(f, dialect="excel")
            column_names: list = next(csv_file)

            for row in csv_file:
                # row[0] is using django's id
                Driver.objects.create(
                    reference=row[1],
                    number=row[2],
                    code=row[3],
                    given_name=row[4],
                    surname=row[5],
                    dob=row[6],
                    nationality=row[7],
                    wiki_url=row[8],
                )

