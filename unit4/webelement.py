__author__ = 'Administrator'


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
# id定位
driver.find_element_by_id("kw").send_keys("selenium自动化")
sleep(2)
driver.find_element_by_id("kw").clear()
# name定位
driver.find_element_by_name("wd").send_keys("python")
driver.refresh()
sleep(2)

driver.get("https://www.51zxw.net/")
driver.back()
driver.forward()

sleep(2)
# link定位
# driver.find_element_by_link_text("计算机等级考试").click()
# sleep(2)
# partial_link_text定位
# driver.find_element_by_partial_link_text("输入法86版").click()
# tag name
driver.find_element_by_tag_name("input").send_keys("selenium")
sleep(5)
# tag names
driver.find_elements_by_tag_name("input")[0].send_keys("appium")
sleep(2)

driver.quit()