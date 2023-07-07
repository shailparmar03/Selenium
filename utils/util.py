import csv
from pathlib import Path

data_file = "data.csv"
cfg_file_dir = "config"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfg_file_dir).joinpath(data_file)


def get_data() -> list:
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = [tuple(row) for row in reader]
    return data


if __name__ == "__main__":
    print(get_data())
