from accweb.rename_old import make_name


def test_make_name():
    assert """2020-02-14 AM - Gen 1 - Nathan Lisulov.mp3""" == make_name("2020-02-14 AM","Gen 1","Nathan Lisulov")
    assert """2020-02-14 PM - Rev 22 vs21 - Daniel Savin.mp3""" == make_name("2020-02-14 PM","Rev 22:21","Daniel Savin")
    assert """2020-02-14 PM - Jovan Lisulov.mp3""" == make_name("2020-02-14 PM",None,"Jovan Lisulov")
    assert """2020-02-14 PM.mp3""" == make_name("2020-02-14 PM",None,None)
    assert """2020-02-14 PM - Matt 1 vs1.mp3""" == make_name("2020-02-14 PM","Matt 1:1",None)

def test_fail():
    assert make_name("2020-02-14 PM","Matt 1:1",None) == """2020-02-14 PM - Matt 1.mp3"""
