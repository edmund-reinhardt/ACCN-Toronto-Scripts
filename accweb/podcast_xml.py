import xml.etree.ElementTree as ET
from datetime import datetime
from glob import glob
from os.path import basename, getsize, join, dirname
from tkinter import filedialog
from xml.dom import minidom

from accweb.metadata import get_metadata
import hashlib

XML_FILE = join(dirname(__file__), "..", "accntoronto_rss.xml")


def add_item(path: str, tree: ET.ElementTree):
    """add the item xml element corresponding to the mp3 file at 'path'
       as a child of the 'tree' element"""
    item = ET.SubElement(tree.find("channel"), 'item')

    scripture, speaker, date, duration = get_metadata(path)
    title = ET.SubElement(item, 'title')
    title_text = f"{speaker} - {scripture}"
    title.text = title_text
    tunes_title = ET.SubElement(item, 'itunes:title')
    tunes_title.text = title_text
    url = f"http://old.accn-toronto.org/media/mp3/sermons/20{date[2:4]}/{basename(path)}"
    link = ET.SubElement(item, 'link')
    link.text = url
    enclosure = ET.SubElement(item, 'enclosure')
    enclosure.set('url', url)
    enclosure.set('length', str(getsize(path)))
    enclosure.set('type', 'audio/mpeg')
    summary = ET.SubElement(item, 'itunes:summary')
    time_of_day = get_verbose_am_pm(date)
    summary.text = f"Sunday {time_of_day} service by {speaker} on {scripture}"
    guid = ET.SubElement(item, 'guid')
    guid.text = hash_file(path)
    seconds: ET.Element = ET.SubElement(item, 'itunes:duration')
    seconds.text = str(round(duration))
    pub_date = ET.SubElement(item, 'pubDate')
    pub_date.text = get_full_date(date)
    return item


def get_verbose_am_pm(date: str) -> str:
    """
    :param date: in the format '2020-01-13 AM'
    :return:  the string 'morning' or 'afternoon' if date ends in 'AM' or 'PM'
    """
    time_day = date.split(" ")[1]
    if time_day == "AM":
        return "morning"
    else:
        return "afternoon"


def get_full_date(date: str):
    """
    Convert date to full published date format expected in RSS XML
    Eastern Standard time assumed, morning services begin as 10:30, afternoon at 14:30
    :param date: in the format '2020-01-15 AM'
    :return: <pubDate> format i.e. 'Sun, 15 Mar 2020 10:30:00 -0500'
    """
    am_or_pm = date.split(" ")
    date_parts = am_or_pm[0].split("-")
    hour = 10
    minutes = 30
    if am_or_pm[1] == "PM":
        hour = 14
    date_time = datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]), hour, minutes)
    return date_time.strftime(f"%a, %d %b %Y %H:%M:%S -0500")


def pretty_print(root: ET.Element) -> str:
    return strip_empty_lines(minidom.parseString(
        ET.tostring(
            root,
            encoding='unicode',
            method="xml"
        )).toprettyxml())


def strip_empty_lines(multi_line: str) -> str:
    return "\n".join([line for line in multi_line.splitlines() if line.strip() != ""])


def parse_rss_xml():
    ET.register_namespace("itunes", "http://www.itunes.com/dtds/podcast-1.0.dtd")
    tree = tree = ET.parse(XML_FILE)
    return tree


def hash_file(name: str) -> str:
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()


def parse_rss_header():
    ET.register_namespace("itunes", "http://www.itunes.com/dtds/podcast-1.0.dtd")
    tree = ET.fromstring(
        """<?xml version="1.0" ?>
<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
    <channel>
        <title>ACC Toronto Services</title>
        <itunes:author>Toronto Apostolic Christian Church (Nazarean)</itunes:author>
        <itunes:owner>
            <itunes:email>accntoronto@gmail.com</itunes:email>
        </itunes:owner>
        <itunes:image href="http://old.accn-toronto.org/media/mp3/sermons/podcastImage.png"/>
        <itunes:summary>
            Sermons and other audio from Apostolic Christian Church in Toronto, ON
        </itunes:summary>
        <language>en</language>
        <itunes:explicit>no</itunes:explicit>
        <link>http://old.accn-toronto.org/sermons</link>
        <itunes:category text="Religion &amp; Spirituality">
            <itunes:category text="Christianity"/>
        </itunes:category>
    </channel>
</rss>""")
    return tree


def write_rss_xml(tree: ET.ElementTree):
    """
    Serialize the given tree into a indented string and write it
    to the accntoronto_rss_xml in the project root
    :param tree: full ElementTree from parsing XMl file
    """
    write_rss_file(pretty_print(tree.getroot()))


def write_rss_file(file_contents:str):
    with open(XML_FILE, "w") as f:
        f.write(file_contents)


def gen_rss_for_all_in_dir(directory: str):
    tree = parse_rss_header()
    for path in glob(join(directory, "*.mp3")):
        print(path)
        add_item(path, tree)
    return pretty_print(tree)


# Generate all of the RSS XML items from the mp3 files in the directory path specified
# through file dialog
if __name__ == '__main__':
    directory = filedialog.askdirectory()
    file_contents = gen_rss_for_all_in_dir(directory)
    write_rss_file(file_contents)
