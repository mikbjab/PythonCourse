import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")

args = parser.parse_args()
input_path = Path(args.input_file)
output_path = Path(args.output_file)
if input_path.exists():
    if input_path.is_file():
        if output_path.exists():
            if output_path.is_file():
                text = input_path.read_text()
                with output_path.open("a") as f:
                    f.write(text)
            else:
                print("Podany plik wyjsciowy nie jest plikiem")
        else:
            print("Podana sciezka pliku wyjsciowego nie istnieje")
    else:
        print("Podany plik wejsciowy nie jest plikiem")
else:
    print("Podana sciezka wejsciowa nie istnieje")
