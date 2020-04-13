from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.51zxw.net/")
driver.maximize_window()

sleep(2)
#最底部
js = "var action = document.documentElement.scrollTop=100000"
driver.execute_script(js)
sleep(2)
# 最顶部
js = "var action = document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(2)
driver.quit()


