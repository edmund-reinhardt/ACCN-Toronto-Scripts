from os.path import basename

import eyed3


def get_metadata(path):
    scripture, speaker = get_scripture_speaker(path)

    return scripture, speaker, get_date(basename(path))


def get_scripture_speaker(path):
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

    return scripture, speaker


def get_date(filename):
    date = f"20{filename[1:3]}-{filename[3:5]}-{filename[5:7]}"

    if filename[8:11] == "000":
        date += " AM"
    elif filename[8:11] == "001":
        date += " PM"

    return date
