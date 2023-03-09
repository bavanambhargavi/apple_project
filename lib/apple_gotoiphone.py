from playwright.sync_api import Page


class GotoIphone():
    iphone_url = "//a[@aria-label='iPhone']//span[@class='globalnav-link-text-container']"
    iphone_13 = "//span[@class='chapternav-label'][normalize-space()='iPhone 13']"


class AppleIphone():

    def __init__(self, page):
        self.page = page

    def clickoniphone(self):
        self.page.locator(GotoIphone.iphone_url).click()
        self.page.locator(GotoIphone.iphone_13).click()

        
    



