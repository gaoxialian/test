__author__ = 'Administrator'
from chandao.common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
base = Base(driver)
# 鼠标移动到“设置”按钮
loc1 = ('link text', '设置')
ele = base.findElement(loc1)
ActionChains(driver).move_to_element(ele).perform()
loc2 = ('link text', '搜索设置')
ele = base.findElement(loc2)
print(ele.is_displayed()) #是否显示该元素--显示True
#------------------hidden元素----------------------
driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
loc3 = ('id', 'hiddenwin')
ele = base.findElement(loc3)
print(ele.is_displayed()) #hidden元素显示为False
# ---------------------不存在的元素显示timeoutException----------------
loc4 = ('id', 'xxx')
ele = base.findElement(loc4)
print(ele.is_displayed()) #hidden元素显示为timeoutException
driver.quit()