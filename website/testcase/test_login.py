__author__ = 'Administrator'
import unittest
from website.testcase.model import function,myunit
from website.testcase.pageobject.LoginPage import LoginPage
from time import sleep

class LoginTest(myunit.StartEnd):

    @unittest.skip
    def test_login1_success(self):
        print("test_login1_success is start run...")
        self.login.login_action('51zxw',123456)
        self.assertEqual(self.login.type_loginPass_hint(),'我的空间')
        function.save_image(self.driver,"51zxw_login1_normal.png")
        print("test_login1_success is end ...")

    def test_login2_pwd_error(self):
        print("test_login2_pwd_error is start run...")
        self.login.login_action('51zxw',123)
        self.assertEqual(self.login.type_loginFail_hint(),'')
        sleep(4)
        function.save_image(self.driver,"51zxw_login1_error.png")
        print("test_login2_pwd_error is end ...")

if __name__ == '__main__':
    unittest.main()
