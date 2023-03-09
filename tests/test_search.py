import time
from lib.search import GotoAppleWebsite


# class AppleWebsite():

def test_searchapple(page):
    apple = GotoAppleWebsite(page)
    time.sleep(3)
    apple.navigate()
    time.sleep(4)
