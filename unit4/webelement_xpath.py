__author__ = 'Administrator'
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
# 定位input标签中为kw的元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys("google")
# 定位input标签中name为wd的元素
driver.find_element_by_xpath("//input[@name='wd']").send_keys("baidu")
# 定位所有标签元素中，class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("搜狗")
sleep(5)
driver.get("https://www.51zxw.net/login")
sleep(3)
# 层级和属性结合$x('//*[@id="loginStr"]')
driver.find_element_by_xpath('//form[@id="loginFrom"]//*[@id="loginStr"]').send_keys("gxl")
driver.find_element_by_xpath("//form[@id='loginFrom']//*[@id='pwd']").send_keys("123456")
# 逻辑运算组合定位
driver.find_element_by_xpath('//input[@id="loginStr" and @name="loginStr"]').send_keys("yyyyy")
sleep(3)
driver.quit()
