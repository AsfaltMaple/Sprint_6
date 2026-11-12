import data
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from locators import order_locators
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


class OrderPage:
    
    def __init__(self, driver):
            self.driver = driver

    def click_order_button(self, button):
        if button == 'top':
            self.driver.find_element(*order_locators.ORDER_BTN_TOP).click()
        elif button == 'bottom':
            self.driver.find_element(*order_locators.ORDER_BTN_BOTTOM).click()

    def check_start_order_header(self):
        return self.driver.find_element(*order_locators.START_ORDER_HEADER).is_displayed()

    def set_name (self, name):
        self.driver.find_element(*order_locators.NAME_FIELD).send_keys(name)

    def set_surname (self, surname):
        self.driver.find_element(*order_locators.SURNAME_FIELD).send_keys(surname)

    
    def set_address (self, address):
        self.driver.find_element(*order_locators.ADDRESS_FIELD).send_keys(address)

    def set_phone (self, phone):
        self.driver.find_element(*order_locators.PHONE_FIELD).send_keys(phone)

    def set_metro_station(self):
        self.driver.find_element(*order_locators.METRO_FIELD).click()
        random.choice(self.driver.find_elements(*order_locators.METRO_STATIONS)).click()

    def click_next_button(self):
        self.driver.find_element(*order_locators.NEXT_BTN).click()

    def set_order_from_date(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y') #эту конструкцию и закрытие календаря эскейпом мне честно подсказал гугл
        self.driver.find_element(*order_locators.ORDER_FROM_FIELD).send_keys(tomorrow)
        self.driver.find_element(*order_locators.ORDER_FROM_FIELD).send_keys(Keys.ESCAPE) 

    def set_rental_period(self):
        self.driver.find_element(*order_locators.RENTAL_PERIOD_FIELD).click()
        random.choice(self.driver.find_elements(*order_locators.RENTAL_PERIODS)).click()

    def click_confirm_order_button(self):
        self.driver.find_element(*order_locators.ORDER_BTN_STEP2).click()

    def check_confirm_order_header(self):
        return self.driver.find_element(*order_locators.CONFIRM_ORDER_HEADER).is_displayed()

    def click_yes_button(self):
        self.driver.find_element(*order_locators.YES_BTN).click()

    def check_success_order_header(self):
        return self.driver.find_element(*order_locators.SUCCESS_ORDER_HEADER).is_displayed()

    def click_check_status_button(self):
        self.driver.find_element(*order_locators.CHECK_STATUS_BTN).click()

    def click_scooter_logo(self):
        self.driver.find_element(*order_locators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*order_locators.YANDEX_LOGO).click()

    def get_current_url(self):
        return self.driver.current_url

    def fill_order_form(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station()
        self.set_phone(phone)
        self.click_next_button()
        self.set_order_from_date()
        self.set_rental_period()
        self.click_confirm_order_button()
        self.click_yes_button()
        self.click_check_status_button()

    def switch_to_new_window(self): #это тоже подсмотрено в гугле, сначала пыталась перенастроить браузер, что в той же вкладке открывался :)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_changes('about:blank'))
        