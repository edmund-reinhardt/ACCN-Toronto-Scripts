from os.path import basename, getsize

import eyed3


def get_metadata(path):
    scripture, speaker, duration = get_scripture_speaker(path)

    return scripture, speaker, get_date(basename(path)), duration


def get_scripture_speaker(path):
    """
    It could be the case that scripture, speaker, or both are none.
    :param path: path to a .mp3 file including the .mp3 extension
    :return: scripture, speaker
    """
    audio_file = eyed3.load(path)
    tag = audio_file.tag

    if tag is None:
        scripture = None
        speaker = None
    else:
        scripture = tag.album
        speaker = tag.artist

    return scripture, speaker, audio_file.info.time_secs


def get_date(filename) -> str:
    """Parses a sermon filename to return a date string, e.g. 2021-01-13 AM"""
    date = f"20{filename[1:3]}-{filename[3:5]}-{filename[5:7]}"

    if filename[8:11] == "000":
        date += " AM"
    elif filename[8:11] == "001":
        date += " PM"

    return date
