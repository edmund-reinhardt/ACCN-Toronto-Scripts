import eyed3
from glob import glob
from os.path import join
from os.path import basename

for path in glob(join("acc_web", "2013", "*.mp3")):
    print(path)

    filename = basename(path)
    print(filename)

    date = f"20{filename[1:3]}-{filename[3:5]}-{filename[5:7]}"

    if filename[8:11] == "000":
        date += " AM"
    elif filename[8:11] == "001":
        date += " PM"

    print(date)

    metadata = eyed3.load(path)

    scripture = metadata.tag.album
    speaker = metadata.tag.artist

    print(scripture)
    print(speaker)

    filename = date

    for item in (scripture, speaker):
        if item is not None:
            filename += " - " + item

    print(filename)
