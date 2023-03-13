from playwright.sync_api import Page


class IphoneFeatures:

    label = '[id="feccf080-c158-11ed-bfb7-0f2f96190cd9"]'
    label_1 = "//label[@for='fecdb3d1-c158-11ed-bfb7-0f2f96190cd9']//img[@class='colornav-swatch']"
    label_2 = "label[id='fece01f0-c158-11ed-bfb7-0f2f96190cd9_label'] span[class='column form-selector-left-col rf-bfe-selector-left-col']"
    label_3 = "//label[@id='noTradeIn_label']"


class AddFeatures:

    def __init__(self, page: Page):
        self.page = page

    def clickonfeatures(self):
        self.page.locator(IphoneFeatures.label).click()
        self.page.locator(IphoneFeatures.label_1).click()
        self.page.locator(IphoneFeatures.label_2).click()
        self.page.locator(IphoneFeatures.label_3).click()
