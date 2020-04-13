from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()

sleep(2)
element = driver.find_element_by_css_selector("#kw")
element.send_keys("python")
sleep(5)
# 全选
element.send_keys(Keys.CONTROL, 'a')
sleep(2)
# 复制
element.send_keys(Keys.CONTROL, "c")
sleep(2)
driver.get("https://www.sogou.com/")
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL, "v")
sleep(5)

driver.quit()
