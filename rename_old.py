from glob import glob
from os import rename
from os.path import basename
from os.path import join
from tkinter import filedialog

import eyed3


def get_date(filename):
    date = f"20{filename[1:3]}-{filename[3:5]}-{filename[5:7]}"

    if filename[8:11] == "000":
        date += " AM"
    elif filename[8:11] == "001":
        date += " PM"

    return date


def make_name(date, scripture, speaker):
    filename = date

    if scripture is not None:
        filename += " - " + scripture.replace(":", " vs")
    if speaker is not None:
        filename += " - " + speaker

    filename += ".mp3"

    return filename


def get_metadata(path):
    """
    It could be the case that scripture, speaker, or both are none.
    :param path: path to a .mp3 file including the .mp3 extension
    :return: scripture, speaker
    """
    metadata = eyed3.load(path).tag

    if metadata is None:
        scripture = None
        speaker = None
    else:
        scripture = metadata.album
        speaker = metadata.artist

    print(scripture)
    print(speaker)

    return scripture, speaker


directory = filedialog.askdirectory()
for path in glob(join(directory, "*.mp3")):
    print(path)

    old_filename = basename(path)
    print(old_filename)

    scripture, speaker = get_metadata(path)
    new_filename = make_name(get_date(old_filename), scripture, speaker)
    print(new_filename)

    new_path = join(directory, new_filename)
    print(new_path)

    rename(path, new_path)