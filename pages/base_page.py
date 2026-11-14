import allure
from locators import base_page_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на логотип самоката')
    def click_scooter_logo(self):
        self.driver.find_element(*base_page_locators.SCOOTER_LOGO).click()
    
    @allure.step('Клик на логотип яндекса')
    def click_yandex_logo(self):
            self.driver.find_element(*base_page_locators.YANDEX_LOGO).click()
    
    @allure.step('Получаем текущий URL')
    def get_current_url(self):
            return self.driver.current_url

    @allure.step('Переключаемся на новое окно браузера')
    def switch_to_new_window(self): #это тоже подсмотрено в гугле, сначала пыталась перенастроить браузер, что в той же вкладке открывался :)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_changes('about:blank'))