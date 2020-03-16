"""Test all the functionality in podcast_xml"""
import xml.etree.ElementTree as ET

def test_get_verbose_am_pm():
    from podcast_xml import get_verbose_am_pm
    assert "morning" == get_verbose_am_pm('2020-10-10 AM')
    assert "afternoon" == get_verbose_am_pm('2020-11-11 PM')


def test_get_full_date():
    from podcast_xml import get_full_date
    assert "Sun, 12 Jan 2020 14:30:00 -0500" == get_full_date('2020-01-12 PM')
    assert "Sun, 19 Jan 2020 10:30:00 -0500" == get_full_date('2020-01-19 AM')


def test_add_item():
    pass