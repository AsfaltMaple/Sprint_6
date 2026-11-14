
import random
import allure
from selenium.webdriver.common.keys import Keys

from locators import order_locators
from datetime import datetime, timedelta
from pages.base_page import BasePage


class OrderPage(BasePage):
    
   
    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_btn(self):
        self.driver.find_element(*order_locators.ORDER_BTN_TOP).click() 

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_buttom_order_btn(self):
        self.driver.find_element(*order_locators.ORDER_BTN_BOTTOM).click()

    @allure.step('Проверяем, что открылась модалка создания заказа')
    def check_start_order_header(self):
        return self.driver.find_element(*order_locators.START_ORDER_HEADER).is_displayed()

    @allure.step('Заполняем поле имени')
    def set_name (self, name):
        self.driver.find_element(*order_locators.NAME_FIELD).send_keys(name)

    @allure.step('Заполняем поле фамилии')
    def set_surname (self, surname):
        self.driver.find_element(*order_locators.SURNAME_FIELD).send_keys(surname)

    @allure.step('Заполняем поле адреса')
    def set_address (self, address):
        self.driver.find_element(*order_locators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Заполняем поле телефона')
    def set_phone (self, phone):
        self.driver.find_element(*order_locators.PHONE_FIELD).send_keys(phone)

    @allure.step('Выбор станции метро')
    def set_metro_station(self):
        self.driver.find_element(*order_locators.METRO_FIELD).click()
        random.choice(self.driver.find_elements(*order_locators.METRO_STATIONS)).click()

    @allure.step('Переход к следующему шагу формы')
    def click_next_button(self):
        self.driver.find_element(*order_locators.NEXT_BTN).click()

    @allure.step('Указываем дату начала аренды')
    def set_order_from_date(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y') #эту конструкцию и закрытие календаря эскейпом мне честно подсказал гугл
        self.driver.find_element(*order_locators.ORDER_FROM_FIELD).send_keys(tomorrow)
        self.driver.find_element(*order_locators.ORDER_FROM_FIELD).send_keys(Keys.ESCAPE) 

    @allure.step('Выбираем период аренды')
    def set_rental_period(self):
        self.driver.find_element(*order_locators.RENTAL_PERIOD_FIELD).click()
        random.choice(self.driver.find_elements(*order_locators.RENTAL_PERIODS)).click()

    @allure.step('Нажимаем на кнопку перехода далее по форме создания заказа')
    def click_confirm_order_button(self):
        self.driver.find_element(*order_locators.ORDER_BTN_STEP2).click()

    @allure.step('Проверяем заголовок окна')
    def check_confirm_order_header(self):
        return self.driver.find_element(*order_locators.CONFIRM_ORDER_HEADER).is_displayed()

    @allure.step('Нажимаем на кнопку подтверждения заказа')
    def click_yes_button(self):
        self.driver.find_element(*order_locators.YES_BTN).click()

    @allure.step('Проверяем заголовок окна')
    def check_success_order_header(self):
        return self.driver.find_element(*order_locators.SUCCESS_ORDER_HEADER).is_displayed()

    @allure.step('Нажимаем на кнопку просмотра заказа')
    def click_check_status_button(self):
        self.driver.find_element(*order_locators.CHECK_STATUS_BTN).click()


    @allure.step('Заполняем форму создания заказа') #кажется предыдущие отдельные действия можно было не размечать шагами, раз уж они тут
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

        