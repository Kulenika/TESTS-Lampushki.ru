
import time
from selenium.webdriver.common.by import By
from Pages.Bronirovanie import BookingPage
from bs4 import BeautifulSoup


def test_booking(browser):
    book_page = BookingPage(browser)
    book_page.visit()
    time.sleep(5)

    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-widget-main')

    calendar_in = browser.find_element(By.CSS_SELECTOR, '#check_in_date')
    book_page.calendar_in.scroll_to_element()
    calendar_in.click()
    time.sleep(3)

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-datepicker')

    time.sleep(3)
    next_btn = browser.find_element(By.CSS_SELECTOR, '#next')

    for i in range(2):
        next_btn.click()
        time.sleep(3)

    check_in_date = browser.find_element(By.CSS_SELECTOR, '#m1r5c1')  # 28.08.2023
    check_in_date.click()
    time.sleep(3)
    check_out_date = browser.find_element(By.CSS_SELECTOR, '#m2r1c5')  #01.09.2023
    check_out_date.click()
    time.sleep(3)

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-widget-main')

    guestchoice_btn = browser.find_element(By.CSS_SELECTOR, '#guest_choice')
    guestchoice_btn.click()
    time.sleep(3)

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-guestchoice')  #Баг. Невозможно выбрать количество детей: в тексте кнопки написано "дети до 0 лет"

    add_adults_btn = browser.find_element(By.CSS_SELECTOR, '#ea_guestchoice_adults_add')  # 2 взрослых
    add_adults_btn.click()
    time.sleep(3)
    close_guestform_btn = browser.find_element(By.CSS_SELECTOR, '#ea_guestchoice_close')
    close_guestform_btn.click()
    time.sleep(3)

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-widget-main')

    search_rooms_btn = browser.find_element(By.CSS_SELECTOR, '#btn-search-rooms')
    search_rooms_btn.click()
    time.sleep(4)

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')

    more_details_btn = browser.find_element(By.CSS_SELECTOR, 'div#button_to_choose[code="1323"]')
    more_details_btn.click()
    time.sleep(4)

    '''проверка результатов поиска (искомое значение:28.08.2023 - 01.09.2023, 2 Adults) '''

    html = '<span class="ea-font-text-p3 primary-text-darken-1" id="room_type_params">28.08.2023 - 01.09.2023, 2 Adults</span>'
    soup = BeautifulSoup(html, 'html.parser')
    room_type_params_value = soup.find('span', {'id': 'room_type_params'}).text
    print(room_type_params_value)

    book_btn = browser.find_element(By.CSS_SELECTOR, 'div#button_to_basket[room_type_code="1323"]')
    book_btn.click()
    time.sleep(3)
    go_to_basket_btn = browser.find_element(By.CSS_SELECTOR, '#go_to_basket > div.go_to_basket_buttons > div.go_to_basket_button2.btn-minor')
    go_to_basket_btn.click()
    time.sleep(3)

    browser.switch_to.frame('ea-widget-main')

    basket_btn = browser.find_element(By.CSS_SELECTOR, '#ea-wdt-basket')
    basket_btn.click()
    time.sleep(3)

    '''Проверка брони 1 номера'''

    html = '<span id="count">1</span>'
    soup = BeautifulSoup(html, 'html.parser')
    count_value = soup.find('span', {'id': 'count'}).text
    print(count_value)
    html = '<span id="rooms" ru="" en="rooms selected">номер</span>'
    soup = BeautifulSoup(html, 'html.parser')
    rooms_selected_value = soup.find('span', {'en': 'rooms selected'}).text
    print(rooms_selected_value)
    html = '<span id="choice" ru="Выбранно" en="">Выбран</span>'
    soup = BeautifulSoup(html, 'html.parser')
    choice_text = soup.find('span', {'id': 'choice'}).text

    if choice_text == 'Выбран':
        print('Выбран.')
    else:
        print('False')

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-prebasket')

    checkout_btn = browser.find_element(By.CSS_SELECTOR, '#btn-desc')
    checkout_btn.click()
    time.sleep(3)

    browser.switch_to.default_content()
    browser.switch_to.frame('ea-module-inline')
    browser.switch_to.frame('ea-prelogin')

    '''Проверка бронирования 1 номера "Глемпинг Лес" с 28.08.2023 по 01.09.2023 (4 ночи) в отеле Шишки на Лампушках'''

    html = '<td data-label="Отель " id="reservation-hotel" lang_data_label="HOTEL"><span>Шишки на Лампушках</span>'
    soup = BeautifulSoup(html, 'html.parser')
    hotel_type_tag = soup.find('td', {'id': 'reservation-hotel'})
    hotel_type = hotel_type_tag.find('span').text
    if hotel_type == 'Шишки на Лампушках':
        print('Отель - Шишки на Лампушках')
    else:
        print('False')

    html = '<td data-label="Тип номера " id="reservation-room-type" lang_data_label="ROOM_TYPE"><span>Глемпинг ЛЕС</span></td>'
    soup = BeautifulSoup(html, 'html.parser')
    room_type_tag = soup.find('td', {'id': 'reservation-room-type'})
    room_type = room_type_tag.find('span').text
    if room_type == 'Глемпинг ЛЕС':
        print('Тип номера - Глемпинг Лес')
    else:
        print('False')

    html = '<td data-label="Дата заезда" id="reservation-check-in" lang_data_label="CHECK_IN_DATE">28.08.2023</td>'
    soup = BeautifulSoup(html, 'html.parser')
    check_in_tag = soup.find('td', {'id': 'reservation-check-in'})
    check_in_date = check_in_tag.string.strip()
    print(check_in_date)

    html = '<td data-label="Ночи" id="reservation-nights" lang_data_label="NIGHTS">4</td>'
    soup = BeautifulSoup(html, 'html.parser')
    night_tag = soup.find('td', {'id': 'reservation-nights'})
    reserv_nights = night_tag.string.strip()
    print(reserv_nights)

    html = '<td data-label="Дата выезда" id="reservation-check-out" langlang_data_label_text="CHECK_OUT_DATE">01.09.2023</td>'
    soup = BeautifulSoup(html, 'html.parser')
    check_out_tag = soup.find('td', {'id': 'reservation-check-out'})
    check_out = check_out_tag.string.strip()
    print(check_out)

    html = '<td data-label="Взрослых" id="reservation-adults" lang_data_label="ADULTS">2</td>'
    soup = BeautifulSoup(html, 'html.parser')
    adults_tag = soup.find('td', {'id': 'reservation-adults'})
    adults_reserv = adults_tag.string.strip()
    print(adults_reserv)

    html = '<td data-label="Дети" id="reservation-childs" lang_data_label="CHILDS">0</td>'
    soup = BeautifulSoup(html, 'html.parser')
    childs_tag = soup.find('td', {'id': 'reservation-childs'})
    childs_reserv = childs_tag.string.strip()
    print(childs_reserv)















































