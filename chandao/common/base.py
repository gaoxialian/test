__author__ = 'Administrator'
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
class Base():

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10

    def findElementNew(self, locator):
        '''定位元素，返回元素对象，没定位到，Timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return ele

    def findElement(self, locator):
        if self.is_tupple(locator):
            ele = WebDriverWait(self.driver, self.timeout).until(lambda x:x.find_element(*locator))
            return ele

    def findElements(self, locator):
        if self.is_tupple(locator):
            eles = WebDriverWait(self.driver, self.timeout).until(lambda x:x.find_elements(*locator))
            return eles

    def sendKeys(self,locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def project_dir(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        return base_dir

    def is_selected(self, locator):
        ele = self.findElement(locator)
        return ele.is_selected()

    def is_title(self, _title):
        try:
            '''返回布尔值'''
            result = WebDriverWait(self.driver, self.timeout).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        try:
            '''返回布尔值'''
            result = WebDriverWait(self.driver, self.timeout).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        try:
            '''返回布尔值'''
            result = WebDriverWait(self.driver, self.timeout).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_alert_present(self):
         try:
            '''判断页面是否有alert，有返回alert(注意这里是返回alert,不是True)没有返回False'''
            result = WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            return result
         except:
             return False

    def get_text(self,locator):
        try:
            r = self.findElement(locator).text
            return r
        except:
            print("获取不到text")
            return ""


    def isElementExsit(self, locator):
        eles = self.findElements(locator)
        _len = len(eles)

        if _len == 1:
            print("存在1个元素", str(locator) )
            return True
        elif _len > 1:
            print("存在多个元素", str(locator) )
            return True
        else:
            print("不存在元素" )
            return False

    def is_tupple(self, locator):
        if not isinstance(locator, tuple):
            print("请输入元祖类型的数据")
            return False
        return True

    '''select 封装'''
    def select_by_index(self, locator, index=0):
        ele = self.findElement(locator)
        Select(ele).select_by_index(index)
        ele.click()

    def select_by_text(self, locator, _text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(_text)

    def select_by_value(self, locator, value):
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

    def is_focus(self, locator):
        '''聚焦定位到某元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def move_to_element(self, locator):
        try:
            ele=self.findElement(locator)
        except TimeoutException as e:
            print("不存在该元素")
        else:
            ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == '__main__':

    loc_user = ('id', '#account')
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    # driver.get("https://www.cnblogs.com/yoyoketang/p/8043814.html")
    driver.get("https://www.baidu.com")
    # loc_user = ('id', 'account')
    # loc_forget_pwd = ('link text', "忘记密码")
    base = Base(driver)
    # loc = ('xpath', ".//*[@id='python36安装sendkeys报错']")
    # base.sendKeys(loc_user,"admin")
    # base.click(loc_forget_pwd)
    # sleep(3)
    # base.js_scroll_end()
    # sleep(2)
    # base.js_scroll_top()
    # sleep(2)
    # # base.is_focus(loc)
    # sleep(2)
    sleep(2)
    loc = ('css selector', "#kw")
    base.move_to_element(loc)

    sleep(2)