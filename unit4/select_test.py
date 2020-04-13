from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


driver = webdriver.Chrome()
driver.get("file:///C:/Users/Administrator/PycharmProjects/webProject/html/selecttest.html")

select = Select(driver.find_element_by_css_selector(".user"))

select.select_by_index(2)
sleep(5)
select.select_by_value("2")
sleep(5)
select.select_by_visible_text("admin")
sleep(5)
driver.quit()
