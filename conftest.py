import pytest
import data
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(data.URL)
    driver.find_element(By.ID, 'rcc-confirm-button').click()
    yield driver
    driver.quit()