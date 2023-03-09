from lib.search import GotoAppleWebsite
from lib.apple_gotoiphone import AppleIphone
import time


def test_gotoiphone(page):
    apple_web = GotoAppleWebsite(page)
    apple_web.navigate()
    apple_iphone = AppleIphone(page)
    apple_iphone.clickoniphone()
    time.sleep(3)




    