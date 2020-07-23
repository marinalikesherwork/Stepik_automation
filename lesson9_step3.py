from selenium import webdriver
import time
import math
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(y)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit() 