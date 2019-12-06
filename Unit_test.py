

from Khaled_Features import Features

def test_siginOut():
    assert  Features.signOut("yes") == 1

def test_AddURL():
    assert  Features.addUrl('https://www.youtube.com')  == 1
#
def test_DownLading():
    assert  Features.downloadFile(None) == 1
#
def test_auth():
    assert  Features.auth(None)  == 1
#
def test_mess():
    assert  Features.AuthMessage("show") == 1
#
def test_RemoveURL():
    assert  Features.removeURL(5) == 1
