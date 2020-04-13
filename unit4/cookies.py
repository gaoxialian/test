from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.51zxw.net/")
driver.add_cookie({'name':"xxxx","value":"cccc"})
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie['name'],cookie['value'])
driver.quit()


