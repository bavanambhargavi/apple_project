from playwright.sync_api import Page


class SearchPage():
    url = "https://www.google.com/"
    locate_apple = "//h3[normalize-space()='Apple (India)']"


class GotoAppleWebsite():

    def __init__(self, page):
        self.page = page
        page.goto(SearchPage.url)
        page.get_by_title("Search").fill("Apple")
        page.keyboard.press("Enter")

    def navigate(self):
        self.page.locator(SearchPage.locate_apple).click()
