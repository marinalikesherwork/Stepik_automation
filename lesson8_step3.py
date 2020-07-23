from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text
    x = str(int(number1) + int(number2))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(x) 
    
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()