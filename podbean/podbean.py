from pathlib import Path
from typing import List

from requests import post, get, put

from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

from secrets import CLIENT_ID, CLIENT_SECRET


def publish(path: Path, title: str):
    size = path.stat().st_size

    print("Getting access token")
    access_token = get_access_token()

    print("Getting presigned upload URL")
    json = get(
        "https://api.podbean.com/v1/files/uploadAuthorize",
        params={
            "access_token": access_token,
            "filename": path.name,
            "filesize": size,
            "content_type": "audio/mpeg",
        },
    ).json()
    presigned_url = json["presigned_url"]
    file_key = json["file_key"]

    print(f"Uploading {path}")
    with open(path, "rb") as f:
        with tqdm(total=size, unit="B", unit_scale=True, unit_divisor=1024) as t:
            wrapped_file = CallbackIOWrapper(t.update, f, "read")
            put(presigned_url, data=wrapped_file)

    print("Publishing episode")
    post(
        "https://api.podbean.com/v1/episodes",
        data={
            "access_token": access_token,
            "title": title,
            "content": "",
            "status": "publish",
            "type": "public",
            "media_key": file_key,
        },
    )


def get_access_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET):
    return post(
        "https://api.podbean.com/v1/oauth/token",
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    ).json()["access_token"]



def _get_titles() -> [str]:
    return [ep["title"] for ep in get_episodes()]


def get_episodes():
    token = get_access_token(CLIENT_ID, CLIENT_SECRET)
    episodes = []
    offset = 0
    while True:
        resp = query_episodes(access_token=token, offset=offset)
        episodes.extend(resp["episodes"])
        if not resp["has_more"]:
            break
        offset += 100

    return episodes


def query_episodes(access_token, offset=0):
    return get(
        "https://api.podbean.com/v1/episodes",
        params={
            "access_token": access_token,
            "offset": offset,
            "limit": 100,
        },
    ).json()


def delete_episode(
    id_: str,
    access_token: str = get_access_token(CLIENT_ID, CLIENT_SECRET),
    delete_media_file=True,
):
    return post(
        f"https://api.podbean.com/v1/episodes/{id_}/delete",
        data={
            "access_token": access_token,
            "delete_media_file": "yes" if delete_media_file else "no",
        },
    ).json()


if __name__ == "__main__":
    delete_episode("9Xmp5EC07ul1", delete_media_file=False)
