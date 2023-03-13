from lib.search import AppleWebsite
from lib.apple_gotoiphone import GotoIphone
from lib.apple_addfeatures import AddFeatures
from playwright.sync_api import Page


def test_addfeatures(page: Page):
    apple = AppleWebsite(page)
    apple.navigate()
    iphone = GotoIphone(page)
    iphone.clickoniphone()
    features = AddFeatures()
    features.clickonfeatures(page)
