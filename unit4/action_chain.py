from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()

sleep(2)
element = driver.find_element_by_css_selector("#kw")
element.send_keys("python")
sleep(5)
# 双击
ActionChains(driver).double_click(element).perform()
sleep(5)
# 右击
ActionChains(driver).context_click(element).perform()
sleep(5)
element = driver.find_element_by_css_selector(".pf")
# 鼠标悬停
ActionChains(driver).move_to_element(element).perform()
sleep(5)
driver.quit()
