__author__ = 'Administrator'
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from chandao.common.base import Base
from time import sleep

driver = webdriver.Chrome()
base = Base(driver)
driver.get("https://www.baidu.com")

r = EC.title_is("百度一下，你就知道")(driver)
r1 = base.is_title("百度一下，你就知道11")
print(r) #True
print(r1) #True

r = EC.title_contains("百度一下")(driver)
r1 = base.is_title_contains("百度一下11")
print(r) #True
print(r1)

loc1 = ('id', "kw")
r = EC.presence_of_element_located(loc1)(driver)
r.send_keys("ccc")
print(r) # 返回WebElement元素对象

driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
loc2 = ('xpath', "//*[@id='login-form']/form/table/tbody/tr[4]/td/a")
r = EC.text_to_be_present_in_element(loc2,"忘记密码")(driver)
print(r) #True
r = base.is_text_in_element(loc2, "忘记密码")


sleep(2)
driver.quit()