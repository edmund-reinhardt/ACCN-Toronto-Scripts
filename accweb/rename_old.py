from glob import glob
from os import rename
from os.path import join
from tkinter import filedialog

from accweb.metadata import get_metadata


def make_name(date, scripture, speaker):
    filename = date

    if scripture is not None:
        filename += " - " + scripture.replace(":", " vs")
    if speaker is not None:
        filename += " - " + speaker

    filename += ".mp3"

    return filename


if __name__ == "__main__":
    directory = filedialog.askdirectory()
    for path in glob(join(directory, "*.mp3")):
        print(path)

        scripture, speaker, date, duration = get_metadata(path)

        new_filename = make_name(date, scripture, speaker)

        new_path = join(directory, new_filename)
        print(new_path)

        rename(path, new_path)
        print()
