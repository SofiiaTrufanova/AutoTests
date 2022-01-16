import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import time
import math


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


links = [
    'https://stepik.org/lesson/236895/step/1', 
    'https://stepik.org/lesson/236896/step/1', 
    'https://stepik.org/lesson/236897/step/1', 
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]

@pytest.mark.parametrize('link', links)
def test_link_success(link, browser):
    browser.get(link)
    browser.implicitly_wait(7)
    answer = math.log(int(time.time()))
    browser.find_element_by_class_name("string-quiz__textarea").send_keys(answer)
    browser.find_element_by_xpath("//button[@class='submit-submission'][contains(.,'Отправить')]").click()
    field = WebDriverWait(browser, 15).until(
        visibility_of_element_located((By.XPATH, "//pre[contains(@class,'hint')]")))
    res = browser.find_element_by_class_name("smart-hints__hint").text      
    assert res == "Correct!", f'Wrong result {res}'
