__author__ = 'Administrator'
from website.testcase.pageobject.BasePage import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    '''新闻登录页面'''
    url = '/news/'

    # 定位器——对相关元素进行定位
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME, 'Submit')

    LoginPass_loc = (By.LINK_TEXT, '我的空间')
    loginFail_loc = (By.NAME, 'username')

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def login_action(self,username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    def type_loginPass_hint(self):
        return self.find_element(*self.LoginPass_loc).text

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text


