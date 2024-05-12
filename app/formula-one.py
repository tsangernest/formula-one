import argparse
import sys
from argparse import ArgumentParser
from typing import NoReturn


def main() -> NoReturn:
    p: ArgumentParser = ArgumentParser()
    p.add_argument("f", type=argparse.FileType("r", encoding="utf-8"))
    arg_input_file = p.parse_args().f

    print(f"\n  :: getting column names from file")
    column_names: list = (arg_input_file
                          .readline()
                          .lower()
                          .strip()
                          .split(sep=",", maxsplit=0))
    print(f" ::: got column names from file!")
    print(f":::: {column_names=}")
    print(f" ::: begin parsing the rest of files")


    print(f"\n\n***End of Processing***\n")
    sys.exit(1)


if __name__ == "__main__":
    main()

