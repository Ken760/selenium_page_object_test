#для запуска теста написать команду
#pytest --language=es test_main_page.py
#language=(выбор языка)
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    sign_in = driver.find_element(
        By.XPATH, "//form[@class='authentication']//input[@type = 'text']"
    )
    sign_in.click()
    sign_in.send_keys('mail' + Keys.TAB + 'password' + Keys.ENTER)
    time.sleep(5)



