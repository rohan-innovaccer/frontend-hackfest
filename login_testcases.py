from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner
import time

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        
    def test_valid_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('Himanch')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('Hello@123')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(home, self.driver.current_url)
        
    def test_empty_values_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_empty_password_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('Himanch')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_empty_username_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('Hello@123')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
    
    def test_invalid_password_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('Himanch')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('Hello@1234')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
    
    def test_invalid_username_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('himanch')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('Hello@123')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_numeric_username_password_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('1233456')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('97734455')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_numeric_username_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('1233456')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('Hello@123')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_numeric_password_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('Himanch')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('97734455')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_symbole_username_password_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('*&^%$#@')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('@#$%^&*')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
    
    def test_symbole_username_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('&*$#@@!')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('Hello@123')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
        
    def test_symbole_password_login(self):
        home = 'http://18.222.121.121:3000/'
        login = 'http://18.222.121.121:3000/login'
        self.driver.get('http://18.222.121.121:3000/')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/nav/ul/li/a')
        element.click()
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[2]/input')
        element.send_keys('Himanch')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/div[4]/input')
        element.send_keys('&*%$#@!!')
        element = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/form/button')
        element.click()
        time.sleep(10)
        self.assertEqual(login, self.driver.current_url)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner)
        
        
        