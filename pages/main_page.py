
from selenium.webdriver.common.by import By
from locators import main_page_locators
from pages.base_page import BasePage

import allure



class MainPage(BasePage):

    
    #def __init__(self, driver):
     #   self.driver = driver

    @allure.step('Проверяем доступность вопроса в списке')
    def check_question_enabled(self, index: int):
        return self.driver.find_element(*main_page_locators.question_id[index]).is_enabled()
    
    @allure.step('Кликнуть на вопрос')
    def click_question(self, index):
        element = self.driver.find_element(*main_page_locators.question_id[index]).click()
        #self.driver.execute_script("arguments[0].click();", element)
    

    @allure.step('Получить текст ответа')
    def get_answer_text(self, index):
        return self.driver.find_element(*main_page_locators.answer_id[index]).text
    
    