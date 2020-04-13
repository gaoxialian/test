from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.51zxw.net/")
driver.maximize_window()
driver.get_screenshot_as_file(r"C:\Users\Administrator\PycharmProjects\webProject\pics\error.png")

driver.quit()


