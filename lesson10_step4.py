from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element_by_xpath("//button[text()='Book']")
button.click()

x = browser.find_element_by_id("input_value").text
y = str(math.log(abs(12*math.sin(int(x)))))
input3 = browser.find_element_by_id("answer")
input3.send_keys(y)
button = browser.find_element_by_xpath("//button[text()='Submit']")
button.click()