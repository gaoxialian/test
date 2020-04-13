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
    loc_get_login_user = ('xpath', ".//*[@id='userMenu']/a")
    loc_refresh_loc = ('xpath', "//a[text()='刷新']")

    def login(self, user='admin', pwd='123456', expected='False', is_keep=False, is_forget=False):
         # 如果点击了忘记密码，则不点击登录按钮
        if is_forget :
            self.click(self.loc_forget_pwd)
            return

        self.input_user(user)
        self.input_pwd(pwd)
        if is_keep : self.input_keep()
        self.click_login_button()


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
        print("获取到的登录用户名为 %s" %user)
        return user

    def is_alert_exsit(self):
        result = self.is_alert_present()
        if result:
            result.accept()
        else:
            print("无存在登录失败弹框！")

    ''' 忘记密码点击之后，判断是否存在刷新按钮 '''
    def is_refresh_exsit(self):
        result = self.isElementExsit(self.loc_refresh_loc)
        return result

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    loginPage = LoginPage(driver)
    loginPage.login()
    print(loginPage.get_login_name())
    # loginPage.sendKeys(self.loc_user)
