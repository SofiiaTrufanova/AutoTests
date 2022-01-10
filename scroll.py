from selenium import webdriver
import math
import time
 
try:  
    link = "http://suninjuly.github.io/execute_script.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("input_value").text
    x = int(num1)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
   
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    option2.click()


    browser.find_element_by_xpath("//button[@type='submit'][contains(.,'Submit')]").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()