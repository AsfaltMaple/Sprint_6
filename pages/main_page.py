
from locators import main_page_locators
from pages.base_page import BasePage

import allure



class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем доступность вопроса в списке')
    def check_question_enabled(self, index: int):
        return self.find_element(main_page_locators.answer_id[index])
   
    
    @allure.step('Кликнуть на вопрос')
    def click_question(self, index):
        self.click_element(main_page_locators.question_id[index])
      

    @allure.step('Получить текст ответа')
    def get_answer_text(self, index):
        return self.get_text(main_page_locators.answer_id[index])
    
    
    