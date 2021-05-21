from ftplib import FTP
from os import listdir, path
from os.path import join, dirname

from accweb.credentials import SERVER, USERNAME, PASSWORD
from accweb.podcast_xml import parse_rss_xml, add_item, write_rss_xml, XML_FILE

# hi marky oh we're use hashtags intresting.  Yes!
# Simulatensouly :D
# we are editing


def sync_sermons(server_name, user_name, password, remote_path, local_path):
    """Upload *.mp3 files in local_path that are not in remote_path"""
    print(f"Connecting to {server_name}")
    with FTP(server_name, user_name, password) as ftp:
        ftp.cwd(remote_path)
        print(f"Change dir {remote_path}")
        local_files = {f for f in listdir(local_path) if f.endswith(".mp3")}
        remote_files = set(ftp.nlst())
        files_to_transfer = list(local_files - remote_files)
        print(f"Found {len(files_to_transfer)} file(s) to transfer")

        tree = parse_rss_xml()

        for f in files_to_transfer:
            full_file_name = join(local_path, f)
            upload(full_file_name, ftp, f)
            print(f"Updating RSS with entry for {f}")
            add_item(full_file_name, tree)

        if len(files_to_transfer) > 0:
            write_rss_xml(tree)
            rss_path, year = path.split(remote_path)
            ftp.cwd(rss_path)
            print(f"Change dir {rss_path}")
            basename = path.basename(XML_FILE)
            upload(XML_FILE, ftp, basename)

    print(f"Done uploading {len(files_to_transfer)}")


def upload(from_path: str, ftp: FTP, to_filename: str):
    print(f"Uploading {to_filename} in {ftp.pwd()}")
    with open(from_path, "rb") as file_contents:
        ftp.storbinary(
            "STOR " + to_filename, file_contents, callback=lambda _: print(".", end="")
        )
    print("Successfully uploaded from " + from_path)


if __name__ == "__main__":
    sync_sermons(
        SERVER,
        USERNAME,
        PASSWORD,
        "/accn-toronto.org/public_html/media/mp3/sermons/2021",
        join(dirname(__file__), "..\..", "2021"),
    )
