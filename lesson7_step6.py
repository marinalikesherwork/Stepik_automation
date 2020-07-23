from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    input2 = browser.find_element_by_id("answer")
    input2.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()