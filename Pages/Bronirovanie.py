from Pages.BasePage import BasePage
from Components.Components import WebElement

class BookingPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://lampushki.ru/bronirovanie'
        super().__init__(driver, self.base_url)
        self.book_form = WebElement(driver, '#ea-widget-main')
        self.calendar_in = WebElement(driver, '#check_in_date')
        self.calendar_out = WebElement(driver, '#check_out_date')
        self.guestchoice = WebElement(driver, '#guest_choice')
        self.search_room = WebElement(driver, '#btn-search-rooms')
        self.basket = WebElement(driver, '#ea-wdt-basket-count')
        self.my_book = WebElement(driver, '#ea-wdt-mybooking')
        self.contact_us = WebElement(driver, 'p > a.el-link')
        self.language = WebElement(driver, '#ea-wdt-language')
        self.room_params_info = WebElement(driver, '#room_type_params')




