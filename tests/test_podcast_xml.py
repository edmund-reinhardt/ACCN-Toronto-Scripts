"""Test all the functionality in podcast_xml"""
from podcast_xml import add_item, parse_rss_xml, pretty_print, strip_empty_lines, get_verbose_am_pm, get_full_date


def test_get_verbose_am_pm():
    assert "morning" == get_verbose_am_pm('2020-10-10 AM')
    assert "afternoon" == get_verbose_am_pm('2020-11-11 PM')


def test_get_full_date():
    assert "Sun, 12 Jan 2020 14:30:00 -0500" == get_full_date('2020-01-12 PM')
    assert "Sun, 19 Jan 2020 10:30:00 -0500" == get_full_date('2020-01-19 AM')


def test_add_item():
    tree = parse_rss_xml()
    add_item("-200126_001.mp3", tree)
    result = pretty_print(tree)
    print(result)


def test_strip_empty_lines():
    assert "a"+"\n"+"b" == strip_empty_lines("\na\nb\n")
