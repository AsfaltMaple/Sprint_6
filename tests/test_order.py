#import pytest
from conftest import driver
import data

import allure
from pages.order_page import OrderPage
from pages.base_page import BasePage


class TestPlaceOrder:

    @allure.title("Проверка оформления заказа самоката через верхнюю кнопку заказа")
    def test_top_order_bnt(self,driver):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        order_page.click_top_order_btn()
        order_page.fill_order_form(*data.order_data_1)
        base_page.click_scooter_logo()

        assert base_page.get_current_url() == data.URL

    @allure.title("Проверка оформления заказа самоката через нижнюю кнопку заказа")
    def test_buttom_order_bnt(self,driver):        
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        order_page.click_buttom_order_btn()
        order_page.fill_order_form(*data.order_data_2)
        base_page.click_yandex_logo()
        base_page.switch_to_new_window()

        assert data.URL_YANDEX in base_page.get_current_url()

