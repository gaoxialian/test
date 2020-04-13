__author__ = 'Administrator'
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from chandao.common.base import Base
from time import sleep

driver = webdriver.Chrome()
base = Base(driver)

driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
loc1 = ('id', "account")
loc2 = ('css selector', '[name="password"]')
loc3 = ('id', 'submit')
base.sendKeys(loc1, '111')
base.sendKeys(loc2, '2222')
base.click(loc3)
r = base.is_alert_present()
r.accept()
print(r)

sleep(2)
driver.quit()