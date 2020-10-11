
import unittest

import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

#including github
class Test_Register_User(unittest.TestCase):

   # @classmethod
   # def setUpClass(cls):
    #    print("###" * 30)
     #   print("I will run once before all test")
     #   print("###" * 30)

    def setUp(self):
        print("I will run once before every test")

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://ndip.co.za/")
        # Check and print link selected by user

    def testCase003_register_with_valid_credentials(self):
        print("Running TestCase A")

        elementByCSS = self.driver.find_element_by_css_selector("a[href='register.html']")
        if elementByCSS is not None:
            print('Registration link is called "' + self.driver.find_element_by_css_selector(
                "a[href='register.html']").text + '"')
            print(self.driver.find_element_by_xpath("//a[@class='navbar-brand']").text)

        self.driver.find_element_by_link_text("Register").click()
        elementByName = self.driver.find_elements_by_link_text("Please Register")
        if elementByName is not None:
            print("User has clicked on register")
        self.driver.find_element_by_id("input-name").send_keys("testautouser")

        # self.driver.find_element_by_xpath(".//*[@id='input-name']").send_keys("test")
        self.driver.find_element_by_css_selector("input[placeholder='Surname']").send_keys("autosurname")
        self.driver.find_element_by_xpath("//input[@id='input-email']").send_keys("testautouser@gmail.com")
        self.driver.find_element_by_css_selector("input[placeholder='Passport Number']").send_keys("A552322113")
        self.driver.find_element_by_id("input-phone").send_keys("08071234569")
        self.driver.find_element_by_css_selector("input[data-bind='value: registrationAddress']").send_keys(
            "Apt 28, Longview drive, Lagos")
        self.driver.find_element_by_xpath(".//*[@id='datereg']").click()
        self.driver.find_element_by_xpath("//div[@class='datepicker-days']//td[@data-date='1527379200000']").click()

        dropdown_gender = Select(self.driver.find_element_by_xpath(".//*[@id='gender']"))
        dropdown_gender.select_by_value("Male")
        dropdown_country = Select(self.driver.find_element_by_xpath(".//*[@id='country']"))
        dropdown_country.select_by_index("2")
        self.driver.find_element_by_id("input-password").send_keys("Password1")
        self.driver.find_element_by_xpath("//input[@id='input-vpassword']").send_keys("Password1")

        # check T&C
        self.driver.find_element_by_xpath("//*[@id='t-and-c-input']").click()

        # wait for a while to complete on captcha
        time.sleep(50)  # seconds

        # filename = "C:\\selenium\\Screenshot\\test.png" #windows format

        # self.driver.find_element_by_xpath(".//*[@id='recaptcha-anchor']/div[5]").click()
        # self.driver.find_element_by_css_selector("div[class='recaptcha-checkbox-checkmark']").click()

        # submit registration

        self.driver.find_element_by_css_selector("button[type='submit']").click()
        # time.sleep(5)

        # try:
        # element_present = EC.visibility_of_element_located((By.XPATH, "//span[@data-notify-text='']"))
        element_present = EC.presence_of_element_located((By.XPATH, "//span[@data-notify-text='']"))
        WebDriverWait(self.driver, 60).until(element_present, message='Registration Terminated' ,)
        if element_present is not None:
            notify = self.driver.find_element_by_xpath("//span[@data-notify-text='']").text
            print(notify)
            notify_success = "You have been successfully registered!"
            print(len(notify))
            print(len(notify_success))
            self.assertEqual(notify, notify_success)
        else:
            self.takeScreenshot()
            # except TimeoutException:
            # except NoSuchElementException:
            # self.assertRaises(NoSuchElementException, self.driver.find_element_by_xpath("//span[@data-notify-text='']"),"Not Found")
            print("Timed out waiting for page to load")
        time.sleep(10)
        timeout = 10

    def testCase004_negative_register_with_existing_user(self):
        print("Running TestCase A")

        elementByCSS = self.driver.find_element_by_css_selector("a[href='register.html']")
        if elementByCSS is not None:
            print('Registration link is called "' + self.driver.find_element_by_css_selector(
                "a[href='register.html']").text + '"')
            print(self.driver.find_element_by_xpath("//a[@class='navbar-brand']").text)

        self.driver.find_element_by_link_text("Register").click()
        elementByName = self.driver.find_elements_by_link_text("Please Register")
        if elementByName is not None:
            print("User has clicked on register")
        self.driver.find_element_by_id("input-name").send_keys("autouser")

        # self.driver.find_element_by_xpath(".//*[@id='input-name']").send_keys("test")
        self.driver.find_element_by_css_selector("input[placeholder='Surname']").send_keys("autotester")
        self.driver.find_element_by_xpath("//input[@id='input-email']").send_keys("autouser@gmail.com")
        self.driver.find_element_by_css_selector("input[placeholder='Passport Number']").send_keys("A902322113")
        self.driver.find_element_by_id("input-phone").send_keys("08071234569")
        self.driver.find_element_by_css_selector("input[data-bind='value: registrationAddress']").send_keys(
            "Apt 28, Longview drive, Lagos")
        self.driver.find_element_by_xpath(".//*[@id='datereg']").click()
        self.driver.find_element_by_xpath("//div[@class='datepicker-days']//td[@data-date='1527379200000']").click()

        dropdown_gender = Select(self.driver.find_element_by_xpath(".//*[@id='gender']"))
        dropdown_gender.select_by_value("Male")
        dropdown_country = Select(self.driver.find_element_by_xpath(".//*[@id='country']"))
        dropdown_country.select_by_index("2")
        self.driver.find_element_by_id("input-password").send_keys("Password1")
        self.driver.find_element_by_xpath("//input[@id='input-vpassword']").send_keys("Password1")

        # check T&C
        self.driver.find_element_by_xpath("//*[@id='t-and-c-input']").click()

        # wait for a while to complete on captcha
        time.sleep(50)  # seconds

        # filename = "C:\\selenium\\Screenshot\\test.png" #windows format

        # self.driver.find_element_by_xpath(".//*[@id='recaptcha-anchor']/div[5]").click()
        # self.driver.find_element_by_css_selector("div[class='recaptcha-checkbox-checkmark']").click()

        # submit registration

        self.driver.find_element_by_css_selector("button[type='submit']").click()
        # time.sleep(5)

        # try:
        # element_present = EC.visibility_of_element_located((By.XPATH, "//span[@data-notify-text='']"))
        element_present = EC.presence_of_element_located((By.XPATH, "//span[@data-notify-text='']"))
        WebDriverWait(self.driver, 60).until(element_present, message='Registration Terminated' ,)
        if element_present is not None:
            notify = self.driver.find_element_by_xpath("//span[@data-notify-text='']").text
            print(notify)
            notify_success = "You have been successfully registered!"
            print(len(notify))
            print(len(notify_success))
            self.assertEqual(notify, notify_success)
        else:
            self.takeScreenshot()
            # except TimeoutException:
            # except NoSuchElementException:
            # self.assertRaises(NoSuchElementException, self.driver.find_element_by_xpath("//span[@data-notify-text='']"),"Not Found")
            print("Timed out waiting for page to load")
        time.sleep(10)
        timeout = 10


    def tearDown(self):
        print("I will run after every test")
        self.driver.close()

   # @classmethod
   # def tearDownClass(cls):
     #   print("###" * 30)
      #  print("I will run once after all test")
      #  print("###" * 30)

    # class to take screenshots
    def takeScreenshot(self):
        driver = self.driver
        filename = "img_" + str(round(time.time() * 1000)) + ".png"  # random number
        screenshotdirectory = "C:\\selenium\\Screenshot\\"  # windows format location and
        destFile = screenshotdirectory + filename
        try:
            driver.save_screenshot(destFile)
            print("Screenshot saved to directory  " + destFile)
        except NotADirectoryError:
            print("Not a directory issue")

if __name__ == '__main__':
    unittest.main(verbosity=2)
   # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\selenium\\NDIP_reports"))


'''
        try:
            element_present = EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "successfully registered"))
            WebDriverWait(self.driver, timeout).until(element_present)
            if element_present is not None:
                print(self.driver.find_element_by_partial_link_text("successfully registered").text)
        except TimeoutException:
            print("Timed out waiting for page to load")
'''

'''

        captchaElement = self.driver.find_element_by_css_selector("#captcha-message")
        if captchaElement is not None:
            print(self.driver.find_element_by_css_selector("#captcha-message").text)
            self.takeScreenshot()

        # self.driver.find_element_by_css_selector("button[type='submit']").click()
        try:
            elementByText = self.driver.find_element_by_partial_link_text("successfully registered")
            if elementByText is not None:
                print(self.driver.find_element_by_partial_link_text("successfully registered").text)
        except NoSuchElementException:
            print("Registration not successful")


    def test_methodA(self):
        print("Running Method A")

    def test_methodB(self):
        print("Running Method B")
    '''


