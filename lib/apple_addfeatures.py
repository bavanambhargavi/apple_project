from playwright.sync_api import Page


class IphoneFeatures():
    label = "//label[@id='9540c5c0-be73-11ed-b20e-a940064a7bc1_label']//span[@class='column form-selector-left-col rf-bfe-selector-left-col']"
    # colour = "//label[@for='3b517eb3-be6e-11ed-86a7-233a13333b4f']//img[@class='colornav-swatch']"
    # storage = "(//span[@class='column form-selector-left-col rf-bfe-selector-left-col'])[3]"


class AddFeatures():

    def __init__(self, page):
        self.page = page

    def clickonfeatures(self):
        self.page.locator(IphoneFeatures.label).click()
        # self.page.locator(IphoneFeatures.colour).click()
        # self.page.locator(IphoneFeatures.storage).click()
