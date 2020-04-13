from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()

driver.implicitly_wait(5)
try:
    WebDriverWait(driver,5, 0.5).until(EC.presence_of_element_located((By.ID,"kw1")))
    element = driver.find_element_by_css_selector("#kw")
    element.send_keys("python")
except NoSuchElementException as e:
    print("无相关元素")
except TimeoutException as e:
    print("等待异常")
sleep(2)

driver.quit()
