__author__ = 'Administrator'
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from chandao.common.base import Base
from time import sleep

driver = webdriver.Chrome()
base = Base(driver)

driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")

loc1 = ('id', 'keepLoginon')
r = EC.text_to_be_present_in_element_value(loc1, "on")(driver)
print(r) #True

loc2 = ('xpath', "//*[@id='login-form']/form/table/tbody/tr[4]/td/a")
ele = base.findElementNew(loc2)
ele.click()

sleep(2)
driver.quit()