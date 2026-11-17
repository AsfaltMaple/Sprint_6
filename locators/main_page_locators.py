from selenium.webdriver.common.by import By

question_id = [(By.ID, f'accordion__heading-{i}') for i in range(8)]
answer_id = [(By.ID, f'accordion__panel-{i}') for i in range(8)]