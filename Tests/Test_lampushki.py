import time
from selenium.webdriver import Keys

from Pages.Lampushki import Lampushki


def test_lampushki(browser):
    lamp_page = Lampushki(browser)
    lamp_page.visit()
    lamp_page.icon.click()
    time.sleep(4)
    browser.set_window_size(2000, 2000)
    time.sleep(2)
    assert lamp_page.equal_url()
    assert lamp_page.promo_video.exist()
    assert browser.title == lamp_page.pageData['title']
    browser.refresh()
    time.sleep(4)
    lamp_page.menu_btn1.exist()
    lamp_page.menu_btn2.exist()
    lamp_page.menu_btn3.exist()
    lamp_page.menu_btn4.exist()
    lamp_page.menu_btn5.exist()
    lamp_page.menu_btn6.exist()
    lamp_page.menu_btn7.exist()
    lamp_page.menu_btn8.exist()
    lamp_page.menu_btn9.exist()
    lamp_page.menu_btn10.exist()
    lamp_page.menu_booking.exist()
    lamp_page.menu_contacts.exist()
    lamp_page.menu_search.exist()

    lamp_page.menu_btn1.click()
    time.sleep(3)
    lamp_page.menu_btn2.click()
    time.sleep(3)
    lamp_page.menu_btn3.click()
    time.sleep(3)
    lamp_page.menu_btn4.click()
    time.sleep(3)
    lamp_page.menu_btn5.click()
    time.sleep(3)
    lamp_page.menu_btn6.click()
    time.sleep(3)
    lamp_page.menu_btn7.click()
    time.sleep(3)
    lamp_page.menu_btn8.click()
    time.sleep(3)
    lamp_page.menu_btn9.click()
    time.sleep(3)
    lamp_page.menu_btn10.click()
    time.sleep(3)
    lamp_page.menu_booking.click()
    time.sleep(5)
    lamp_page.menu_contacts.click()
    time.sleep(5)
    lamp_page.button_language.exist()
    lamp_page.button_language.click()
    time.sleep(4)


def test_search(browser):
    lamp_page = Lampushki(browser)
    lamp_page.visit()
    time.sleep(3)
    browser.set_window_size(2000, 2000)
    time.sleep(2)
    lamp_page.menu_search.click()
    time.sleep(4)
    lamp_page.close_btn.click()
    time.sleep(3)
    lamp_page.menu_search.click()
    time.sleep(2)
    lamp_page.search_text.send_keys('Проживание')
    time.sleep(2)
    lamp_page.search_text.send_keys(Keys.ENTER)
    time.sleep(3)











