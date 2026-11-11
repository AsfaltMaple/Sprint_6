
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import main_page_locators


class MainPage:

    
    def __init__(self, driver):
        self.driver = driver

    def check_question_enabled(self, index: int):
        return self.driver.find_element(*main_page_locators.question_id.format(index)).is_enabled()
    
    def click_question(self, index):
        element = self.driver.find_element(By.ID, main_page_locators.question_id.format(index))
        self.driver.execute_script("arguments[0].click();", element)
        element.click()

    def get_answer_text(self, index):
        return self.driver.find_element(By.ID, main_page_locators.answer_id.format(index)).text
    
    