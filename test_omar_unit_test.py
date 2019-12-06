import Omar_Unit_Test

def test_sortAscending():
    assert Omar_Unit_Test.sortAscending('ascending') == 1

def test_sortDescending():
    assert Omar_Unit_Test.sortDescending('Descending') == 1

def test_sortDatAscending():
    assert Omar_Unit_Test.sortDatAscending('ascending') == 1


def test_sortDateDescending():
    assert Omar_Unit_Test.sortDateDescending('Descending') == 1


def test_sortChannelAscending():
    assert Omar_Unit_Test.sortChannelAscending('ascending') == 1


def test_sortChanelDescending():
    assert Omar_Unit_Test.sortChanelDescending('Descending') == 1