
def test_get_verbose_am_pm():
    from podcast_xml import get_verbose_am_pm
    assert "morning" == get_verbose_am_pm('2020-10-10 AM')
    assert "afternoon" == get_verbose_am_pm('2020-11-11 PM')


def test_get_full_date():
    from podcast_xml import get_full_date
    # get_full_date()
