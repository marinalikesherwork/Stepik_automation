from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("1")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("2")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("3")
    element = browser.find_element_by_id("file")
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()