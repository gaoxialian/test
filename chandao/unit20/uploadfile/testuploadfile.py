__author__ = 'Administrator'

from selenium import webdriver
from chandao.page.login_page import LoginPage
from time import sleep
from pykeyboard import PyKeyboard
from pymouse import PyMouse

loc1 = ('xpath', '//*[@id="dataform"]/table//*[@title="图片"]')
loc_liulan = ('css selector', '.ke-upload-button')
loc_sure = ('xpath', '//input[@type="button" and @value="确定"]')

loc_test = ('link text', '测试')
loc_bug = ('link text', 'Bug')
loc_add_bug = ('xpath', "//*[@id='createActionMenu']/a")

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:82/zentao/bug-create-1-0-moduleID=0.html")
login = LoginPage(driver)
login.login()
login.click(loc_test)
login.click(loc_bug)
login.click(loc_add_bug)
login.click(loc1)
sleep(2)
login.click(loc_liulan)

keybord = PyKeyboard()
sleep(10)
keys = r"D:\workspace\pics\1.jpg"
for i in keys:
    keybord.tap_key(i)

sleep(3)
keybord.tap_key(keybord.enter_key)
keybord.tap_key(keybord.enter_key)
sleep(5)


login.click(loc_sure)
# driver.quit()


# driver.quit()