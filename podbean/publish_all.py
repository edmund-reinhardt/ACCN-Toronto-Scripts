from glob import glob
from os.path import join
from pathlib import Path
from time import sleep

from podbean import publish, get_episodes
from sermons import get_metadata, create_title

INPUT_DIR = "data/sermons"

print("Retrieving all episodes")
episodes = get_episodes()
# filenames = [ep["media_url"].split("/")[-1] for ep in episodes]
titles = [ep["title"] for ep in episodes]


def attempt_publish(path: Path):
    speaker, scripture = get_metadata(path)

    if not speaker or not scripture:
        return

    title = create_title(scripture, speaker)
    if title in titles:
        print(f"Episode {title} already exists, skipping...")
        return

    print(f"Publishing {path}")
    publish(path, title)


for path in list((Path(p) for p in glob(join(INPUT_DIR, "**.mp3")))):
    while True:
        try:
            attempt_publish(path)
            break
        except Exception as e:
            print(e)
            sleep(5)
