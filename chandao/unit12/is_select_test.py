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
loc2 = ('link text', '搜索设置')
loc3 = ('xpath', "//*[@id='nr']/option[1]")
loc4 = ('xpath', "//*[@id='nr']/option[3]")
driver.implicitly_wait(10)
driver.maximize_window()
ele = base.findElement(loc1)
ActionChains(driver).move_to_element(ele).perform()
base.click(loc2)
# select
ele2 = base.findElement(loc3)
ele3 = base.findElement(loc4)
print(ele2.is_selected()) # 默认选择第一个 True
print(ele3.is_selected()) # 第三个未被选中False

driver.quit()