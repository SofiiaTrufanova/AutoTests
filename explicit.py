from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
browser.find_element_by_id("book").click()

num2 = browser.find_element_by_id("input_value").text
x = int(num2)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

browser.find_element_by_xpath ("//button[@type='submit'][contains(.,'Submit')]").click()

