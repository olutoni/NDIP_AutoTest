'''
Created on Jun 3, 2018

@author: oluto
'''

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class Register():

    def test_success_reg(self):
        print("Running TestCase A")

        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://ndip.co.za/")
        #Check and print link selected by user
        elementByCSS = driver.find_element_by_css_selector("a[href='register.html']")
        if elementByCSS is not None:
            print('Registration link is called "' + driver.find_element_by_css_selector("a[href='register.html']").text+'"')

        driver.find_element_by_link_text("Register").click()
        elementByName= driver.find_elements_by_link_text("Please Register")
        if elementByName is not None:
            print("User has clicked on register")
        driver.find_element_by_id("input-name").send_keys("newuser")
        #driver.find_element_by_xpath(".//*[@id='input-name']").send_keys("test")
        driver.find_element_by_css_selector("input[placeholder='Surname']").send_keys("tester")
        driver.find_element_by_xpath("//input[@id='input-email']").send_keys("newuser@gmail.com")
        driver.find_element_by_css_selector("input[placeholder='Passport Number']").send_keys("A402322113")
        driver.find_element_by_id("input-phone").send_keys("08071234569")
        driver.find_element_by_css_selector("input[data-bind='value: registrationAddress']").send_keys("Apt 28, Longview drive, Lagos")
        driver.find_element_by_xpath(".//*[@id='datereg']").click()
        driver.find_element_by_xpath("//div[@class='datepicker-days']//td[@data-date='1527379200000']").click()

        dropdown_gender = Select(driver.find_element_by_xpath(".//*[@id='gender']"))
        dropdown_gender.select_by_value("Male")
        dropdown_country = Select(driver.find_element_by_xpath(".//*[@id='country']"))
        dropdown_country.select_by_index("2")
        driver.find_element_by_id("input-password").send_keys("Password1")
        driver.find_element_by_xpath("//input[@id='input-vpassword']").send_keys("Password1")

        #check T&C
        driver.find_element_by_xpath("//*[@id='t-and-c-input']").click()

        #wait for a while to complete on captcha
        time.sleep(10) #seconds

       # filename = "C:\\selenium\\Screenshot\\test.png" #windows format


        #driver.find_element_by_xpath(".//*[@id='recaptcha-anchor']/div[5]").click()
        #driver.find_element_by_css_selector("div[class='recaptcha-checkbox-checkmark']").click()

        #submit registration

        driver.find_element_by_css_selector("button[type='submit']").click()

        captchaElement = driver.find_element_by_css_selector("#captcha-message")
        if captchaElement is not None:
            print(driver.find_element_by_css_selector("#captcha-message").text)
            self.takeScreenshot(driver)

    #class to take screenshots
    def takeScreenshot(self,driver):
        filename = "img_"+str(round(time.time()*1000))+".png" #random number
        screenshotdirectory = "C:\\selenium\\Screenshot\\"  # windows format location and
        destFile = screenshotdirectory + filename
        try:
            driver.save_screenshot(destFile)
            print("Screenshot saved to directory  " + destFile)
        except NotADirectoryError:
            print("Not a directory issue")

'''
        timeout = 120 #seconds
        try:
            element_present = EC.presence_of_element_located((By.XPATH, "//div[@style='border: medium none;']"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        
 '''
ff = Register()
ff.test_success_reg()

