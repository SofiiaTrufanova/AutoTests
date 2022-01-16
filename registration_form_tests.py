import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#link = "http://suninjuly.github.io/registration1.html"

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()    

    def test1(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration1.html")
        input1 = driver.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("a@gmail.com")
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        
    def test2(self):
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration2.html")
        input1 = driver.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("a@gmail.com")
        button = driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


