import eyed3
from glob import glob
from os.path import join
from os.path import basename
from os import rename


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

    return filename


for directory in glob(join("acc_web", "*")):
    print(directory)
    for path in glob(join(directory, "*.mp3")):
        print(path)

        filename = basename(path)
        print(filename)

        metadata = eyed3.load(path).tag

        if metadata is None:
            scripture = None
            speaker = None
        else:
            scripture = metadata.album
            speaker = metadata.artist

        print(scripture)
        print(speaker)

        filename = make_name(get_date(filename), scripture, speaker)

        print(filename)

        new_path = join(directory, filename)

        print(path)
        print(new_path)

        rename(path, new_path)
