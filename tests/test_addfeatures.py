from lib.search import GotoAppleWebsite
from lib.apple_gotoiphone import AppleIphone
from lib.apple_addfeatures import AddFeatures


def test_addfeatures(page):
    apple = GotoAppleWebsite(page)
    apple.navigate()
    iphone = AppleIphone(page)
    iphone.clickoniphone()
    features = AddFeatures(page)
    features.clickonfeatures()


