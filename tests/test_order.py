import pytest
from conftest import driver
import data

import allure
from pages.order_page import OrderPage
from pages.base_page import BasePage


class TestPlaceOrder:

    @pytest.mark.parametrize('order_data, button', [
    (data.order_data_1, 'top'),
    (data.order_data_2, 'bottom')])

    @allure.title("Проверка оформления заказа самоката")
    def test_order_scooter_positive(self, driver, order_data, button):
        name, surname, address, phone = order_data

        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        order_page.click_order_button(button)

        order_page.fill_order_form(name, surname, address, phone)
        base_page.click_scooter_logo()

        assert base_page.get_current_url() == data.URL

        base_page.click_yandex_logo()
        base_page.switch_to_new_window()

        assert data.URL_YANDEX in base_page.get_current_url()

