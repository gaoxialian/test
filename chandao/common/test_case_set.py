__author__ = 'Administrator'

import unittest
from selenium import webdriver
from chandao.page.login_page import LoginPage
from chandao.page.add_bug_page import AddBugPage
class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html")
        cls.login = LoginPage(cls.driver)
        cls.bug = AddBugPage(cls.driver)
        cls.login.login()

    def setUp(self):
       self.driver.get("http://127.0.0.1:82/zentao/my/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
