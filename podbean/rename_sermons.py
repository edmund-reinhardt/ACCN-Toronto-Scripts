from glob import glob
from os.path import join
from pathlib import Path
from shutil import copyfile
from shutil import rmtree
from os.path import exists
from os import mkdir

from sermons import get_date, get_metadata

INPUT_DIR = "data/sermons"
OUTPUT_DIR = "data/processed_sermons"

if exists(OUTPUT_DIR):
    rmtree(OUTPUT_DIR)
mkdir(OUTPUT_DIR)

for path in (Path(p) for p in glob(join(INPUT_DIR, "**.mp3"))):
    artist, album = get_metadata(path)

    if not artist or not album:
        continue

    filename = path.name
    year, month, day = get_date(filename)
    new_filename = f"{year}-{month}-{day}_{artist}_{album}"
    print(new_filename)

    copyfile(path, join(OUTPUT_DIR, new_filename))
