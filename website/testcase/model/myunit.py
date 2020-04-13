__author__ = 'Administrator'
import unittest
from driver import *
from website.testcase.pageobject.LoginPage import LoginPage
class StartEnd(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()