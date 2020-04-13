from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.51zxw.net/")
driver.maximize_window()

sleep(2)
selenium_index = driver.current_window_handle
sleep(2)
driver.find_element_by_partial_link_text("远程培训班").click()
sleep(2)
driver.switch_to.window(selenium_index)
sleep(2)
driver.find_element_by_partial_link_text("与您同").click()
sleep(2)
driver.quit()


