from playwright.sync_api import Page


class CheckIphone:

    Iphone_loc = "//a[@aria-label='iPhone']//span[@class='globalnav-link-text-container']"
    Iphone13 = "//span[@class='chapternav-label'][normalize-space()='iPhone 13']"


class GotoIphone:

    def __init__(self, page: Page):
        self.page = page

    def clickoniphone(self):
        self.page.wait_for_timeout(3000)
        self.page.locator(CheckIphone.Iphone_loc).click()
        self.page.locator(CheckIphone.Iphone13).click()
