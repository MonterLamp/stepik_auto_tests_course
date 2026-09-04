from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    browser.get(link)

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100"))
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[id='solve']").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
