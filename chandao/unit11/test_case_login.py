__author__ = 'Administrator'
import unittest
from chandao.unit11.login_page import LoginPage
from selenium import webdriver
import ddt
import os
from chandao.common.excel_util import ExcelUtil
@ddt.ddt
class TestLogin(unittest.TestCase):

    base_dir = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(base_dir,'data', 'users.xlsx')
    excel = ExcelUtil(filepath)
    data= excel.dict_data()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginPage = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.htm")
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.idata(data)
    def test_login1_success(self,data):
        print(data)
        self.loginPage.login(data['user'],data['pwd'],data['expected'])


if __name__ == '__main__':
    unittest.main()