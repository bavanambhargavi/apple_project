from playwright.sync_api import Page


class AddBag:

    loc_1 = "[id=applecareplus_58_noapplecare_label]"
    loc_2 = "//button[@title='Add to Bag']"
    loc_3 = "//button[normalize-space()='Review Bag']"


class AddtoBag:

    def __init__(self, page: Page):
        self.page = page

    def clickaddtobag(self):
        self.page.locator(AddBag.loc_1).click()
        self.page.locator(AddBag.loc_2).click()
        self.page.locator(AddBag.loc_3).click()
