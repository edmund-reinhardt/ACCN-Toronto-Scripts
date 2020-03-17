"""Test all the functionality in podcast_xml"""
from podcast_xml import add_item, parse_rss_xml, pretty_print, strip_empty_lines, get_verbose_am_pm, get_full_date


def test_get_verbose_am_pm():
    assert "morning" == get_verbose_am_pm('2020-10-10 AM')
    assert "afternoon" == get_verbose_am_pm('2020-11-11 PM')


def test_get_full_date():
    assert "Sun, 12 Jan 2020 14:30:00 -0500" == get_full_date('2020-01-12 PM')
    assert "Sun, 19 Jan 2020 10:30:00 -0500" == get_full_date('2020-01-19 AM')


def test_strip_empty_lines():
    assert "a"+"\n"+"b" == strip_empty_lines("\na\nb\n")


def test_add_item():
    tree = parse_rss_xml()
    add_item("-200126_001.mp3", tree)
    result = pretty_print(tree)
    assert """<?xml version="1.0" ?>
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
		<link>http://accn-toronto.org</link>
		<itunes:category text="Religion &amp; Spirituality"/>
		<item>
			<title>Phillip Denzinger - John 16</title>
			<enclosure url="http://accn-toronto.org/media/mp3/sermons/2020/-200126_001.mp3" length="24780946" type="audio/x-mp3"/>
			<itunes:summary>Sunday afternoon service by Phillip Denzinger on John 16</itunes:summary>
			<pubDate>Sun, 26 Jan 2020 14:30:00 -0500</pubDate>
		</item>
	</channel>
</rss>""" == result