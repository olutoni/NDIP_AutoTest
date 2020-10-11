'''
Created on Jun 3, 2018

@author: oluto
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#import unittest

import pytest

#@pytest.fixture()
#class RegisterUser():
    #    def setUp(self):
    #        print("I will run once before every test")
@pytest.fixture()
def setUp():
    print("Running demo1 setUp")
    
def test_validReg(setUp):
    print("Running TestCase A")
            
    driver = webdriver.Firefox()
    driver.get("https://ndip.co.za/")
            
    #       print(driver.find_element_by_css_selector("a[href='register.html']").is_displayed)
    print(driver.find_element_by_css_selector("a[href='register.html']").text)
            
    driver.find_element_by_link_text("Register").click()
    driver.find_element_by_id("input-name").send_keys("testuser")
    driver.find_element_by_css_selector("input[placeholder='Surname']").send_keys("tester")
    driver.find_element_by_xpath("//input[@id='input-email']").send_keys("testuser@gmail.com")
    driver.find_element_by_css_selector("input[placeholder='Passport Number']").send_keys("A002322113")
    driver.find_element_by_id("input-phone").send_keys("08071234567")
    driver.find_element_by_css_selector("input[data-bind='value: registrationAddress']").send_keys("Apt 28, Longview drive, Lagos")
    driver.find_element_by_xpath(".//*[@id='datereg']").click()
    driver.find_element_by_xpath("//div[@class='datepicker-days']//td[@data-date='1527379200000']").click()
         
    dropdown_gender = Select(driver.find_element_by_xpath(".//*[@id='gender']"))
    dropdown_gender.select_by_value("Male")
            
    driver.find_element_by_id("input-password").send_keys("Password1")
    driver.find_element_by_xpath("//input[@id='input-vpassword']").send_keys("Password1")
       
        #dropdown_country = Select(driver.find_element_by_xpath(".//*[@id='country']"))
        #dropdown_country.select_by_index(index)
          
        #driver.find_element_by_css_selector("input[placeholder='Password']").clear()
        #driver.implicitly_wait(15)
        #driver.find_element_by_css_selector("input[placeholder='Password']").send_keys("password")

        #driver.find_element_by_class_name("btn login-btn").click()
        #driver.find_element_by_css_selector("button[type='submit']").click()
        #print(driver.find_element_by_css_selector("button[type='submit']").text)
        #driver.find_element_by_css_selector("input[placeholder='Password']").clear()
        
        #driver.find_element_by_xpath("//input[@placeholder='Password']").clear()
#stepA = RegisterUser()
#stepA.test_validReg()
    
#    def test_methodB(self):
#        print("Running Method B")
        
#    def tearDown(self):
#        print("I will run once after every test")

#if __name__ == '__main__':
#    unittest.main(verbosity=2)


