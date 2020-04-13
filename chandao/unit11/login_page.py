__author__ = 'Administrator'
from chandao.common.base import Base
from selenium import webdriver
from time import sleep
class LoginPage(Base):

    loc_user = ('id', 'account')
    loc_pwd = ('css selector', '[name="password"]')
    loc_keep= ('id', 'keepLoginon')
    loc_button = ('id', 'submit')
    loc_forget_pwd = ('link text', "忘记密码")
    loc_get_login_user = ('xpath', ".//*[@id='userMenu']/a/i")

    def login(self, user='admin', pwd='123456', expected='False', is_keep=False):
        self.input_user(user)
        self.input_pwd(pwd)
        if is_keep : self.input_keep()
        sleep(2)
        self.click_login_button()
        sleep(2)

    def input_user(self, text):
        self.sendKeys(self.loc_user, text)

    def input_pwd(self, text):
        self.sendKeys(self.loc_pwd, text)

    def input_keep(self):
        self.findElement(self.loc_keep)

    def click_login_button(self):
        self.click(self.loc_button)

    def get_login_name(self):
        user = self.get_text(self.loc_get_login_user)
        return user

    def is_alert_exsit(self):
        result = self.is_alert_present()
        if result:
            result.accept()
        else:
            print("无存在登录失败弹框！")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    loginPage = LoginPage(driver)
    # loginPage.sendKeys(self.loc_user)
