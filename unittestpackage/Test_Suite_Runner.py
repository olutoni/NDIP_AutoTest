import unittest
import HTMLTestRunner
from unittest import TestLoader, TestSuite

import os

from test_case_demo import Test_User_Registration
from user_registration import Test_Register_User

dir = os.getcwd()

# get all tests from test_case_demo and user_registration class
first_tests = TestLoader().loadTestsFromTestCase(Test_User_Registration)
second_tests = TestLoader().loadTestsFromTestCase(Test_Register_User)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([first_tests, second_tests])

# configure HTMLTestRunner options


outfile = open(dir + "\SmokeTestReport.html", "wb")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
stream=outfile,
title='Test Report',
description='Smoke Tests'
)

# run the suite using HTMLTestRunner
runner.run(smoke_tests)

