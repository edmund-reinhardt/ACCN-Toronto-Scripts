from pathlib import Path

from tinytag import TinyTag


def get_date(filename: str):
    if filename.startswith("-"):
        year = "20" + filename[1:3]
        month = filename[3:5]
        day = filename[5:7]
    else:
        year = filename[:4]
        month = filename[5:7]
        day = filename[8:10]

    return year, month, day


def get_metadata(path: Path):
    tag = TinyTag.get(path.resolve())
    return tag.artist, tag.album


def create_title(scripture: str, speaker: str):
    return f"{speaker} - {scripture}"
