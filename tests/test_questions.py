
import pytest
from conftest import driver
import data

from locators import main_page_locators
from pages import main_page
from pages.main_page import MainPage 

class TestTextAnswer:

    @pytest.mark.parametrize("index, expected_text", list(enumerate(data.expected_answers)))

    def test_check_answer_text(self, driver, index, expected_text):
        main_page = MainPage(driver)
        main_page.click_question(index)
        answer_text = main_page.get_answer_text(index)
        assert answer_text == expected_text