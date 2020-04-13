__author__ = 'Administrator'
import time,unittest
from selenium import webdriver
from chandao.common.test_case_set import StartEnd
import ddt
import os
from chandao.common.excel_util import ExcelUtil

base_dir = os.path.dirname(os.path.dirname(__file__))
filepath = os.path.join(base_dir,'data', 'users.xlsx')
excel = ExcelUtil(filepath)
data= excel.dict_data()

'''登录cases'''
@ddt.ddt
class TestLogin(StartEnd):
    ''' login suites '''
    def setUp(self):
        self.login.is_alert_exsit()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    '''
        登录根据excel中的数据进行输入
    '''
    @ddt.idata(data)
    def test_login_case1(self,data):
        '''用例说明：登录根据excel中的数据进行输入'''
        self.login.login(data['user'],data['pwd'],data['expected'])
        result = self.login.get_login_name()
        self.assertTrue(result == data['expected'])

    ''' 登录点击忘记密码'''
    def test_login_case2(self):
        '''用例说明：忘记密码点击'''
        self.login.login(is_forget = True)
        result = self.login.is_refresh_exsit()
        self.assertTrue(result)
        # self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

