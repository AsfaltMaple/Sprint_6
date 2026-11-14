from selenium.webdriver.common.by import By

ORDER_BTN_TOP = (By.XPATH, "(//button[contains(@class, 'Button_Button')])[1]")
ORDER_BTN_BOTTOM = (By.XPATH, "(//button[contains(@class, 'Button_Button')])[3]")

NEXT_BTN = (By.XPATH, "//button[text()='Далее']")
PREV_BTN = (By.XPATH, "//button[text()='Назад']")

START_ORDER_BTN = (By.XPATH, "(//button[contains(@class, 'Button_Button') and text()='Заказать'])[2]")
ORDER_BTN_STEP2 = (By.XPATH, "(//button[contains(@class, 'Button_Button') and text()='Заказать'])[2]")
YES_BTN = (By.XPATH, "//button[text()='Да']")
CHECK_STATUS_BTN = (By.XPATH, "//button[text()='Посмотреть статус']")


NAME_FIELD = (By.XPATH, "//*[contains(@placeholder, 'Имя')]")
SURNAME_FIELD = (By.XPATH, "//*[contains(@placeholder, 'Фамилия')]")
ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
METRO_FIELD = (By.XPATH, "//*[contains(@placeholder, 'метро')]")
PHONE_FIELD = (By.XPATH, "//*[contains(@placeholder, 'Телефон')]")
ORDER_FROM_FIELD = (By.XPATH, "//*[contains(@placeholder, 'Когда привезти самокат')]")
RENTAL_PERIOD_FIELD = (By.XPATH, "//div[contains(@class, 'Dropdown')]")
RENTAL_PERIODS = (By.CSS_SELECTOR, 'div.Dropdown-option')
METRO_STATIONS = (By.CSS_SELECTOR, "li.select-search__row") #чертов пропадающий список, откуда не выцепить локатор!!!

#оставлю себе коммент о поиске локатора, это не закомменченный код, а чтобы не потерять: 
# def set_metro_station(self): - заменить метод заполнения метро с неправильным локатором на этот, и потом искать в сообщении об ошибке элементы вокруг "Сокольники"
    #metro = self.driver.find_element(*order_locators.METRO_FIELD)
    #metro.click()
    #metro.send_keys("Сокольники")
    #print(self.driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML"))

START_ORDER_HEADER = (By.XPATH, "//div[contains(@class,'Order_Header')]")

CONFIRM_ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
SUCCESS_ORDER_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")


