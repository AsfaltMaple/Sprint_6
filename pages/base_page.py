import random
from allure import step
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys


class BasePage:

    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver


    def find_element(self, locator, timeout=TIMEOUT):
        with step (f'Найти элемент {locator}'):
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=TIMEOUT):
        with step (f'На элемент {locator} можно кликнуть'):
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator, timeout=TIMEOUT):
        with step(f'Кликнуть на {locator}'):
            self.find_element(locator, timeout).click()

    def get_text(self, locator, timeout=TIMEOUT):
        with step(f'Получить текст {locator}'):
            return self.find_element(locator, timeout).text

    def set_text(self, locator, text):
        with step (f'Заполнить поле значением {text}'):
            self.find_element(locator).send_keys(text)

    def choose_element_from_list(self, field_locator, elements_locator):
        with step (f'Выбор значения из списка'):
            self.click_element(field_locator)
            elements = WebDriverWait(self.driver, timeout=self.TIMEOUT).until(EC.presence_of_all_elements_located(elements_locator))
            random.choice(elements).click()


    def set_tomorrow_date(self, locator):
        with step (f'Выбрать дату из календаря'):
            tomorrow = (datetime.now() + timedelta(days=1)).strftime('%d.%m.%Y')
            self.find_element(locator).send_keys(tomorrow)
            self.find_element(locator).send_keys(Keys.ESCAPE)

    def get_url(self):
        with step(f'Получить url'):
            return self.driver.current_url()

    def switch_to_new_window(self):
        with step(f'Переключиться на новую вкладку'):
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, 10).until(EC.url_changes('about:blank'))
         

