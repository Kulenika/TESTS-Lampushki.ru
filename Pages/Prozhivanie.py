from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Components.Components import WebElement

class ProzhivaniePage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://lampushki.ru/prozhivanie'
        super().__init__(driver, self.base_url)

        self.glamping_about_btn = WebElement(driver, 'div.jsHeightFixRow.uk-grid.item-row-1 > div.item-column.uk-width-large-1-3.first > div > div > div > div:nth-child(6) > a')
        self.glamping_about_text = WebElement(driver, 'div.jsHeightFixRow.uk-grid.item-row-1 > div.item-column.uk-width-large-1-3.first > div > div > div > div.uk-height-min-medium > div.item-text.uk-divider > div')
        self.glamping_compare_btn = WebElement(driver, '#compare-502159 > div.jbcompare-unactive > span')
        self.glamping_quickview_btn = WebElement(driver, 'a#quickview-241425')