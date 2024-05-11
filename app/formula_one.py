import sys
from fileinput import FileInput, input
from pathlib import Path


def main() -> None:

    fp: FileInput = input(files="../formula-1-data-set/drivers.csv", mode="r", encoding="utf-8")

    print(fp.filename())

    print(f"\n\n***End of Processing***\n")
    sys.exit(1)


if __name__ == "__main__":
    main()

