from ftplib import FTP
from os import listdir
from os.path import join

from credentials import SERVER, USERNAME, PASSWORD
from podcast_xml import parse_rss_xml, add_item, write_rss_xml, XML_FILE


def sync_sermons(server_name, user_name, password, remote_path, local_path):
    """Upload *.mp3 files in local_path that are not in remote_path"""
    print(f"Connecting to {server_name}")
    with FTP(server_name, user_name, password) as ftp:
        ftp.cwd(remote_path)

        local_files = {f for f in listdir(local_path) if f.endswith(".mp3")}
        remote_files = set(ftp.nlst())
        files_to_transfer = list(local_files - remote_files)
        print(f"Found {len(files_to_transfer)} file(s) to transfer")

        tree = parse_rss_xml()

        for f in files_to_transfer:
            print(f"Uploading {f}")
            with open(join(local_path, f), "rb") as file_contents:
                ftp.storbinary('STOR ' + f, file_contents, callback=lambda _: print(".", end=""))
            add_item(local_path, tree)

        if len(files_to_transfer) != 0:
            write_rss_xml(tree)
            with open(join(XML_FILE, f), "rb") as file_contents:
                ftp.storbinary('STOR ' + f, file_contents, callback=lambda _: print(".", end=""))

    print(f"Done uploading {len(files_to_transfer)}")


if __name__ == '__main__':
    sync_sermons(
        SERVER,
        USERNAME,
        PASSWORD,
        "/public_html/media/mp3/sermons/2020",
        "2020"
    )
