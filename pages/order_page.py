
import allure

from locators import order_locators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

   
    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_btn(self):
        self.click_element(order_locators.ORDER_BTN_TOP)

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_buttom_order_btn(self):
        self.click_element(order_locators.ORDER_BTN_BOTTOM)

    @allure.step('Проверяем, что открылась модалка создания заказа')
    def check_start_order_header(self):
        self.find_element(order_locators.START_ORDER_HEADER)

    @allure.step('Заполняем поле имени')
    def set_name (self, name):
        self.set_text(order_locators.NAME_FIELD, name)

    @allure.step('Заполняем поле фамилии')
    def set_surname (self, surname):
        self.set_text(order_locators.SURNAME_FIELD, surname)

    @allure.step('Заполняем поле адреса')
    def set_address (self, address):
        self.set_text(order_locators.ADDRESS_FIELD, address)

    @allure.step('Заполняем поле телефона')
    def set_phone (self, phone):
        self.set_text(order_locators.PHONE_FIELD, phone)

    @allure.step('Выбор станции метро')
    def set_metro_station(self):
        self.choose_element_from_list(order_locators.METRO_FIELD, order_locators.METRO_STATIONS)
        
    @allure.step('Переход к следующему шагу формы')
    def click_next_button(self):
        self.click_element(order_locators.NEXT_BTN)

    @allure.step('Указываем дату начала аренды')
    def set_order_from_date(self):
        self.set_tomorrow_date(order_locators.ORDER_FROM_FIELD)

    @allure.step('Выбираем период аренды')
    def set_rental_period(self):
        self.choose_element_from_list(order_locators.RENTAL_PERIOD_FIELD, order_locators.RENTAL_PERIODS)

    @allure.step('Нажимаем на кнопку перехода далее по форме создания заказа')
    def click_confirm_order_button(self):
        self.click_element(order_locators.ORDER_BTN_STEP2)

    @allure.step('Проверяем заголовок окна')
    def check_confirm_order_header(self):
        return self.find_element(order_locators.CONFIRM_ORDER_HEADER)

    @allure.step('Нажимаем на кнопку подтверждения заказа')
    def click_yes_button(self):
        self.click_element(order_locators.YES_BTN)

    @allure.step('Проверяем заголовок окна')
    def check_success_order_header(self):
        return self.find_element(order_locators.SUCCESS_ORDER_HEADER)

    @allure.step('Нажимаем на кнопку просмотра заказа')
    def click_check_status_button(self):
        self.click_element(order_locators.CHECK_STATUS_BTN)

    @allure.step('Клик на логотип')
    def click_scooter_logo(self):
        self.click_element(order_locators.SCOOTER_LOGO)

    @allure.step('Клик на логотип')
    def click_yandex_logo(self):
        self.click_element(order_locators.YANDEX_LOGO)

    @allure.step('Переключение вкладки после клика на лого яндекса')
    def switch_to_yandex_window(self):
        return self.switch_to_new_window()

    @allure.step('Получить URL')
    def get_current_url(self):
        return self.get_url()


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

        