import xml.etree.ElementTree as ET
from glob import glob
from os.path import basename, getsize, join
from tkinter import filedialog
from xml.dom import minidom

from metadata import get_metadata


def add_item(path: str, parent: ET.Element):
    scripture, speaker, date = get_metadata(path)
    item = ET.SubElement(parent, 'item')

    title = ET.SubElement(item, 'title')
    title.text = f"{date}: {speaker} - {scripture}"
    enclosure = ET.SubElement(item, 'enclosure')
    enclosure.set('url', f"http://accn-toronto.org/media/mp3/sermons/2020/{basename(path)}")
    enclosure.set('length', str(getsize(path)))
    enclosure.set('type', 'audio/x-mp3')
    summary = ET.SubElement(item, 'itunes:summary')
    summary.text = f"Sunday service by {speaker} on {scripture}"

    return item


def pretty_print(root: ET.Element) -> str:
    return minidom.parseString(
        ET.tostring(
            root,
            encoding='unicode',
            method="xml"
        )).toprettyxml()


# Generate all of the RSS XML items from the mp3 files in the directory path specified
# through file dialog
if __name__ == '__main__':
    ET.register_namespace("itunes", "http://www.itunes.com/dtds/podcast-1.0.dtd")
    xml_file = 'accntoronto_rss.xml'
    tree = ET.parse(xml_file)

    directory = filedialog.askdirectory()
    for path in glob(join(directory, "*.mp3")):
        print(path)
        add_item(path, tree.getroot()[0])

    with open(xml_file, "w") as f:
        f.write(pretty_print(tree.getroot()))
