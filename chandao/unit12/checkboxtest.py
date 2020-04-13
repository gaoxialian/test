__author__ = 'Administrator'
from chandao.common.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/PycharmProjects/webProject/html/select+checkbox.html")
base = Base(driver)

loc1 = ('id', 'c1')
loc2 = ('id', 'c2')

print(base.is_selected(loc1))
print(base.is_selected(loc2))

loc3 = ('css selector', '[type="checkbox"]')
eles = base.findElements(loc3)
for ele in eles:
    r = []
    is_select = ele.is_selected()
    if not is_select:
        ele.click()
    r.append(is_select)
print(r)

sleep(2)

driver.quit()

