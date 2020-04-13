from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/PycharmProjects/webProject/html/selecttest.html")
sleep(2)
driver.find_elements_by_tag_name("option")[2].click()
sleep(2)
driver.find_element_by_css_selector("[value='1']").click()
sleep(5)
driver.quit()
