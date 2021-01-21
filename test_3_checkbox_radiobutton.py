from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elemetn = browser.find_element_by_id("input_value")
    x = x_elemetn.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    check = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    check.click()

    radio = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except:
    pass

