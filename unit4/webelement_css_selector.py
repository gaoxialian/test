__author__ = 'Administrator'
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
# 根据id定位
driver.find_element_by_css_selector("#kw").send_keys("google")
sleep(2)
# 根据class吃定位
driver.find_element_by_css_selector(".s_ipt").send_keys("baidu")
# sleep(2)
# 根据属性来定位
driver.find_element_by_css_selector('[autocomplete="off"]').send_keys("搜狗")
sleep(2)
# 根据元素层级来定位
driver.find_element_by_css_selector("form#form>span>input#kw").send_keys("111")
sleep(5)

driver.quit()
