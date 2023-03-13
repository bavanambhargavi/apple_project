from lib.search import AppleWebsite
from lib.apple_gotoiphone import GotoIphone 
from lib.apple_addfeatures import AddFeatures
from lib.apple_addtothebag import AddtoBag
from lib.apple_traceviewer import TraceViewer
from playwright.sync_api import Page


def test_traceviewer(page: Page):
    apple = AppleWebsite(page)
    apple.navigate()
    iphone = GotoIphone(page)
    iphone.clickoniphone()
    features = AddFeatures(page)
    features.clickonfeatures()
    bag = AddtoBag(page)
    bag.clickaddtobag()
    viewer = TraceViewer(page)
    viewer.traceviewer()

