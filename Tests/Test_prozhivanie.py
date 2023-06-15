import time
from Pages.Prozhivanie import ProzhivaniePage

def test_prozhivanie(browser):
    page2 = ProzhivaniePage(browser)
    page2.visit()
    assert page2.equal_url()


