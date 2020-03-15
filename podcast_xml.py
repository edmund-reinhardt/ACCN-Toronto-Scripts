import xml.etree.ElementTree as ET
from datetime import datetime
from glob import glob
from os.path import basename, getsize, join
from tkinter import filedialog
from xml.dom import minidom

from metadata import get_metadata

XML_FILE = 'accntoronto_rss.xml'


def add_item(path: str, tree: ET.ElementTree):
    """add the item xml element corresponding to the mp3 file at 'path'
       as a child of the 'tree' element"""
    item = ET.SubElement(tree.getroot().find("channel"), 'item')

    scripture, speaker, date = get_metadata(path)
    title = ET.SubElement(item, 'title')
    title.text = f"{speaker} - {scripture}"
    enclosure = ET.SubElement(item, 'enclosure')
    enclosure.set('url', f"http://accn-toronto.org/media/mp3/sermons/2020/{basename(path)}")
    enclosure.set('length', str(getsize(path)))
    enclosure.set('type', 'audio/x-mp3')
    summary = ET.SubElement(item, 'itunes:summary')
    time_of_day = get_verbose_am_pm(date)
    summary.text = f"Sunday {time_of_day} service by {speaker} on {scripture}"

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
    am_or_pm = date.split(" ")
    date_parts = am_or_pm[0].split("-")
    date_time = datetime(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
    date_time = date_time.replace(minute=30)  # , tzinfo='EST')
    if am_or_pm[1] == "AM":
        date_time = date_time.replace(hour=10)
    else:
        date_time = date_time.replace(hour=14)
    return date_time.strftime(f"%a, %d %b %Y %H:%M:%S -0500")


def pretty_print(root: ET.Element) -> str:
    return minidom.parseString(
        ET.tostring(
            root,
            encoding='unicode',
            method="xml"
        )).toprettyxml()


def parse_rss_xml():
    ET.register_namespace("itunes", "http://www.itunes.com/dtds/podcast-1.0.dtd")
    tree = ET.parse(XML_FILE)
    return tree


def write_rss_xml(tree: ET.ElementTree):
    with open(XML_FILE, "w") as f:
        f.write(pretty_print(tree.getroot()))


# Generate all of the RSS XML items from the mp3 files in the directory path specified
# through file dialog
if __name__ == '__main__':
    tree = parse_rss_xml()

    directory = filedialog.askdirectory()
    for path in glob(join(directory, "*.mp3")):
        print(path)
        add_item(path, tree)

    write_rss_xml(tree)
