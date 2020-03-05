import xml.etree.ElementTree as ET
from os.path import basename, getsize
from metadata import get_metadata


def create_item_for_mp3(path):
    scripture, speaker, date = get_metadata(path)
    scripture, speaker, date = get_metadata(path)
    item = ET.Element('item')

    title = ET.SubElement(item, 'title')
    title.text = f"{date}: {speaker} - {scripture}"
    enclosure = ET.SubElement(item, 'enclosure')
    enclosure.set('url', f"http://accn-toronto.org/media/mp3/sermons/2020/{basename(path)}")
    enclosure.set('length', str(getsize(path)))
    enclosure.set('type', 'audio/x-mp3')
    summary = ET.SubElement(item, 'itunes:summary')
    summary.text = f"Sunday service by {speaker} on {scripture}"
    return item

if __name__ == '__main__':
    # tree = ET.parse('accntoronto_rss.xml')
    #
    # print('Hi')
    # print(tree.findall("./channel/item"))
    # channel = tree.find("./rss/channel")
    # print(channel)
    # for item in tree.getroot().iter('item'): print(item.attrib)
    path = 'C:\\Users\\Nlisu\\OneDrive\\Desktop\\Current Courses\\Side Project with Church\\ACCN-Toronto-Scripts\\-160103_000.mp3'
    item = create_item_for_mp3(path)
    ET.dump(item)
