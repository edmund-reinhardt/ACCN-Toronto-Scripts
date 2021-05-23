"""Test all the functionality in podcast_xml"""
from os.path import join, dirname

RSS_XML_SAMPLE = """<?xml version="1.0" ?>
<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
	<channel>
		<title>ACC Toronto Services</title>
		<itunes:author>Toronto Apostolic Christian Church (Nazarean)</itunes:author>
		<itunes:owner>
			<itunes:email>accntoronto@gmail.com</itunes:email>
		</itunes:owner>
		<itunes:image href="http://accn-toronto.org/media/mp3/sermons/podcastImage.png"/>
		<itunes:summary>
            Sermons and other audio from Apostolic Christian Church in Toronto, ON
        </itunes:summary>
		<language>en</language>
		<itunes:explicit>no</itunes:explicit>
		<link>http://accn-toronto.org/sermons</link>
		<itunes:category text="Religion &amp; Spirituality">
			<itunes:category text="Christianity"/>
		</itunes:category>
		<item>
			<title>Phillip Denzinger - John 16</title>
			<itunes:title>Phillip Denzinger - John 16</itunes:title>
			<link>http://accn-toronto.org/media/mp3/sermons/2020/-200126_001.mp3</link>
			<enclosure url="http://accn-toronto.org/media/mp3/sermons/2020/-200126_001.mp3" length="24780946" type="audio/mpeg"/>
			<itunes:summary>Sunday afternoon service by Phillip Denzinger on John 16</itunes:summary>
			<guid>8a2e05eeecd4e9810370226eb7e740f5186ee555</guid>
			<itunes:duration>1236</itunes:duration>
			<pubDate>Sun, 26 Jan 2020 14:30:00 -0500</pubDate>
		</item>
	</channel>
</rss>"""
from accweb.podcast_xml import add_item, parse_rss_xml, pretty_print, strip_empty_lines, get_verbose_am_pm, \
    get_full_date, gen_rss_for_all_in_dir, parse_rss_header, hash_file


def test_get_verbose_am_pm():
    assert "morning" == get_verbose_am_pm('2020-10-10 AM')
    assert "afternoon" == get_verbose_am_pm('2020-11-11 PM')


def test_get_full_date():
    assert "Sun, 12 Jan 2020 14:30:00 -0500" == get_full_date('2020-01-12 PM')
    assert "Sun, 19 Jan 2020 10:30:00 -0500" == get_full_date('2020-01-19 AM')


def test_strip_empty_lines():
    assert "a" + "\n" + "b" == strip_empty_lines("\na\n\nb\n")


def test_hash_file():
    assert "8a2e05eeecd4e9810370226eb7e740f5186ee555" == hash_file(join(dirname(__file__), "-200126_001.mp3"))


def test_add_item_2020():
    import xml.etree.ElementTree as ET
    tree = parse_rss_header()
    item = add_item(join(dirname(__file__), "-200126_001.mp3"), tree)
    expected_item = '<item>' \
            '<title>Phillip Denzinger - John 16</title>' \
            '<itunes:title>Phillip Denzinger - John 16</itunes:title>' \
            '<link>http://accn-toronto.org/media/mp3/sermons/2020/-200126_001.mp3</link>' \
            '<enclosure url="http://accn-toronto.org/media/mp3/sermons/2020/-200126_001.mp3" length="24780946" type="audio/mpeg" />' \
            '<itunes:summary>Sunday afternoon service by Phillip Denzinger on John 16</itunes:summary>' \
            '<guid>8a2e05eeecd4e9810370226eb7e740f5186ee555</guid>' \
            '<itunes:duration>1236</itunes:duration>' \
            '<pubDate>Sun, 26 Jan 2020 14:30:00 -0500</pubDate>' \
            '</item>'
    assert ET.tostring(item, encoding='unicode', method="xml") == \
        expected_item
    result = pretty_print(tree)
    assert result == RSS_XML_SAMPLE


def test_gen_rss_for_all_in_dir():
    assert gen_rss_for_all_in_dir(dirname(__file__)) == RSS_XML_SAMPLE


def test_add_item_2021():
    import xml.etree.ElementTree as ET
    tree = parse_rss_header()
    item = add_item(join(dirname(__file__), "-210126_001.mp3"), tree)
    expected_item = '<item>' \
            '<title>Phillip Denzinger - John 16</title>' \
            '<itunes:title>Phillip Denzinger - John 16</itunes:title>' \
            '<link>http://accn-toronto.org/media/mp3/sermons/2021/-210126_001.mp3</link>' \
            '<enclosure url="http://accn-toronto.org/media/mp3/sermons/2021/-210126_001.mp3" length="24780946" type="audio/mpeg" />' \
            '<itunes:summary>Sunday afternoon service by Phillip Denzinger on John 16</itunes:summary>' \
            '<guid>8a2e05eeecd4e9810370226eb7e740f5186ee555</guid>' \
            '<itunes:duration>1236</itunes:duration>' \
            '<pubDate>Tue, 26 Jan 2021 14:30:00 -0500</pubDate>' \
            '</item>'
    assert ET.tostring(item, encoding='unicode', method="xml") == \
        expected_item
