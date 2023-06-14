import time
from Pages.Prozhivanie import ProzhivaniePage

def test_prozhivanie(browser):
    page2 = ProzhivaniePage(browser)
    page2.visit()
    assert page2.equal_url()
    page2.glamping_about_btn.scroll_to_element()
    page2.glamping_quickview_btn.click()
    time.sleep(3)
    page2.glamping_about_btn.click()
    time.sleep(3)
    browser.back()
    time.sleep(3)
    browser.forward()
    time.sleep(3)



