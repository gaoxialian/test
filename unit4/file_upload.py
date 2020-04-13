from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector(".soutu-btn").click()
sleep(2)
driver.find_element_by_css_selector(".upload-pic").send_keys(r'D:\workspace\pics\1.jpg')

sleep(2)
driver.quit()


