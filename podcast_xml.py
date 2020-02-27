import xml.etree.ElementTree as ET

from metadata import get_metadata


def create_item_for_mp3(path):
    scripture, speaker, date = get_metadata(path)


if __name__ == '__main__':
    # tree = ET.parse('accntoronto_rss.xml')
    #
    # print('Hi')
    # print(tree.findall("./channel/item"))
    # channel = tree.find("./rss/channel")
    # print(channel)
    # for item in tree.getroot().iter('item'): print(item.attrib)
    path = 'C:\\Users\\EDMUNDReinhardt\\accweb\\2020\\-200223_001.mp3'
    scripture, speaker, date = get_metadata(path)
    item = ET.Element('item')

    title = ET.SubElement(item, 'title')
    title.text = f"{date}: {speaker} - {scripture}"
    ET.dump(item)
