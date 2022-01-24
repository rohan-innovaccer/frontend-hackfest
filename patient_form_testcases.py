from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import time

class PatientForm(unittest.TestCase):
    
    def test_empty_age_patient_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000/')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/i').click()
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/div[2]/input')
        ele.clear()
        ele.send_keys('kishore')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[3]/div[2]/div/button/div')
        time.sleep(1)
        ele.click()
        ele = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div')
        time.sleep(2)
        ele.click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
    
    def test_empty_name_patient_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000/')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/i').click()
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('22')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
      
    def test_valid_patient_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000/')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/i').click()
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('kishore')
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[2]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele.send_keys('22')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[3]/div[2]/div/button/div').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        time.sleep(5)
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div').text
        time.sleep(5)
        self.assertIn(valid_message, value)
        self.driver.close()
        
    def test_empty_details_patient_form(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://18.222.121.121:3000/')
        self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input').send_keys('Himanch')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input').send_keys('Hello@123')
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/i').click()
        valid_message = 'Submitted Successfully'
        invalid_message = 'invalid details'
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[1]/div[2]/input')
        time.sleep(1)
        ele.clear()
        ele = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div/div[2]/div[2]/input')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/button').click()
        time.sleep(1)
        value = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div').text
        time.sleep(5)
        self.assertIn(invalid_message, value)
        self.driver.close()
    
   
        
    
    
# if __name__ == "__main__":
#     unittest.main()
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner)
        