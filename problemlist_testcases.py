from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import time
from selenium.webdriver.common.keys import Keys

class ProblemList(unittest.TestCase):
    
    def test_empty_problemlist_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        ele.click()
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        ele.send_keys('Himanch')
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        ele.send_keys('Hello@123')
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        ele.click()
        time.sleep(3)
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[5]/div/i')
        ele.click()
        time.sleep(2)
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/input')
        ele.clear()
        ele.send_keys('')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('')
        
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/span').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
    
    def test_empty_date_of_site_problemlist_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        ele.click()
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        ele.send_keys('Himanch')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        ele.send_keys('Hello@123')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        ele.click()
        time.sleep(3)
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[5]/div/i')
        ele.click()
        time.sleep(2)
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/input')
        ele.clear()
        ele.send_keys('Cerebral Palsy')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('torso')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[2]/div/div[1]/input')
        time.sleep(1)
        ele.clear()
        
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[4]/div[2]/div/button/div')
        ele.click()
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div')
        ele.click()
        
        ele = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div[1]/div[5]/div[2]/div/button/div')
        ele.click()
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div')
        ele.click()
        
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/span').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
    
    def test_empty_bodyofsite_problemlist_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[5]/div/i').click()
        time.sleep(2)
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/input')
        ele.clear()
        ele.send_keys('Cerebral Palsy')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('')
        
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[2]/div/div[1]/input')
        ele.click()
        time.sleep(5)
        ele.send_keys(8*Keys.BACK_SPACE) 
        time.sleep(2)        
        for i in '07012021':
            ele.send_keys(i)
    
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/span').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
      
    def test_empty_diagnosis_name_problemlist_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//html/body/div/div/div/div[1]/div/div/div[1]/div/div[5]/div/i').click()
        time.sleep(2)
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/input')
        ele.clear()
        ele.send_keys('')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('torso')
        
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/span').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
        
    def test_valid_problemlist_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//html/body/div/div/div/div[1]/div/div/div[1]/div/div[5]/div/i').click()
        time.sleep(2)
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[1]/div[2]/input')
        ele.clear()
        ele.send_keys('Cerebral Palsy')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('torso')
        
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[3]/div[2]/div/div[1]/input')
        ele.click()
        time.sleep(5)
        ele.send_keys(8*Keys.BACK_SPACE) 
        time.sleep(2)        
        for i in '07012021':
            ele.send_keys(i)
        
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[1]/div[4]/div[2]/div/button/div')
        ele.click()
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div')
        ele.click()
        
        ele = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div[1]/div[5]/div[2]/div/button/div')
        ele.click()
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div')
        ele.click()
        
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div/div/span').text
        time.sleep(5)
        self.assertIn(valid_message, value)
        self.driver.close()
        
    
    
if __name__ == "__main__":
    unittest.main()
# if __name__ == "__main__":
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner)
        