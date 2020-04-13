from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/PycharmProjects/webProject/html/alert.html")
driver.maximize_window()

driver.find_element_by_id("add").click()
sleep(2)
alert = driver.switch_to_alert()
alert.accept()
sleep(2)
driver.quit()


