import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_exist_button(browser):
    browser.get(link)
    time.sleep(30)
    buttons = browser.find_elements(By.XPATH, "//button[@class = 'btn btn-lg btn-primary btn-add-to-basket']")
    print(buttons)
    assert len(buttons) > 0, 'Кнопки не найдено'
