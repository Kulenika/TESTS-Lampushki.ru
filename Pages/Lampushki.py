
from Pages.BasePage import BasePage
from Components.Components import WebElement

class Lampushki(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://lampushki.ru/'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'Главная - Заповедный мир Шишки на Лампушке'
        }
        self.icon = WebElement(driver, 'div.uk-navbar-container > nav > div.uk-navbar-center > a > img')
        self.promo_video = WebElement(driver, '#module-102 > div.uk-section-default.uk-section-overlap.uk-cover-container.uk-section.uk-section-large.uk-flex.uk-flex-middle > video')
        self.menu_btn1 = WebElement(driver, 'div.uk-navbar-center-left.uk-preserve-width > div > ul > li.item-121.uk-parent > a')

        self.menu_btn2 = WebElement(driver, 'div.uk-navbar-center-left.uk-preserve-width > div > ul > li.item-180.uk-parent > a')

        self.menu_btn3 = WebElement(driver, 'div.uk-navbar-center-left.uk-preserve-width > div > ul > li.item-181.uk-parent > a')
        self.menu_btn4 = WebElement(driver, 'div.uk-navbar-center-left.uk-preserve-width > div > ul > li.item-256.uk-parent > a')
        self.menu_btn5 = WebElement(driver, 'div.uk-navbar-center-left.uk-preserve-width > div > ul > li.item-331 > a')
        self.menu_btn6 = WebElement(driver, 'div.uk-navbar-center-left.uk-preserve-width > div > ul > li.item-334 > a')
        self.menu_btn7 = WebElement(driver, 'div.uk-navbar-center-right.uk-preserve-width > div > ul > li.item-147.uk-parent > a')
        self.menu_btn8 = WebElement(driver, 'div.uk-navbar-center-right.uk-preserve-width > div > ul > li.item-185.uk-parent > a')
        self.menu_btn9 = WebElement(driver, 'div.uk-navbar-center-right.uk-preserve-width > div > ul > li.item-295.uk-parent > a')
        self.menu_btn10 = WebElement(driver, 'div.uk-navbar-center-right.uk-preserve-width > div > ul > li.item-328 > a')
        self.menu_booking = WebElement(driver, 'div.uk-navbar-center-right.uk-preserve-width > div > ul > li.item-259 > a')
        self.menu_contacts = WebElement(driver, 'div.uk-navbar-center-right.uk-preserve-width > div > ul > li.item-258 > a')
        self.menu_search = WebElement(driver, '#module-tm-1 > a')
        self.close_btn = WebElement(driver, '#search-tm-1-modal > div > button')
        self.search_text = WebElement(driver, '#search-tm-1 > input.uk-search-input.uk-text-center')
        self.button_language = WebElement(driver, '#module-99 > div > div > a')


    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

