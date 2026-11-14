
#from selenium.webdriver.common.by import By
from locators import main_page_locators
from pages.base_page import BasePage

import allure



class MainPage(BasePage):


    @allure.step('Проверяем доступность вопроса в списке')
    def check_question_enabled(self, index: int):
        return self.driver.find_element(*main_page_locators.question_id[index]).is_enabled()
    
    @allure.step('Кликнуть на вопрос')
    def click_question(self, index):
        self.driver.find_element(*main_page_locators.question_id[index]).click()
      

    @allure.step('Получить текст ответа')
    def get_answer_text(self, index):
        return self.driver.find_element(*main_page_locators.answer_id[index]).text
    
    