from glob import glob
from os.path import join
from pathlib import Path

from podbean import get_episodes, delete_episode
from sermons import get_metadata, create_title

INPUT_DIR = "data/sermons"


episodes = get_episodes()
uploaded_filenames = [ep["media_url"].split("/")[-1] for ep in episodes]
uploaded_title = [ep["title"] for ep in episodes]

filenames = [Path(p).name.replace(" ", "-") for p in glob(join(INPUT_DIR, "**.mp3"))]

print(len(filenames), len(set(filenames)))
print(len(uploaded_filenames), len(set(uploaded_filenames)))

for p in [Path(p) for p in glob(join(INPUT_DIR, "**.mp3"))]:
    speaker, scripture = get_metadata(p)
    title = create_title(scripture, speaker)

    normalized_filename = p.name.replace(" ", "-")
    if normalized_filename not in uploaded_filenames:
        print(p.name, title in uploaded_title)

print(
    len(
        [
            p
            for p in glob(join(INPUT_DIR, "**.mp3"))
            if Path(p).name.replace(" ", "-") not in uploaded_filenames
        ]
    )
)
