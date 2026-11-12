import pytest
from conftest import driver
import data

import allure
from pages.order_page import OrderPage


class TestPlaceOrder:

    @pytest.mark.parametrize('order_data, button', [
    (data.order_data_1, 'top'),
    (data.order_data_2, 'bottom')])

    @allure.title("Проверка оформления заказа самоката")
    def test_order_scooter_positive(self, driver, order_data, button):
        name, surname, address, phone = order_data

        order_page = OrderPage(driver)
        order_page.click_order_button(button)

        order_page.fill_order_form(name, surname, address, phone)
        order_page.click_scooter_logo()

        assert order_page.get_current_url() == data.URL

        order_page.click_yandex_logo()
        order_page.switch_to_new_window()

        assert data.URL_YANDEX in order_page.get_current_url()

