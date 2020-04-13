__author__ = 'Administrator'

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:82/zentao/user-login.html")
sleep(2)
js = '$("#account").val("admin")'
driver.execute_script(js)
js2 = '''$("[name='password']").val(123456)'''
driver.execute_script(js2)
sleep(3)
js3='''$("#keepLoginon").click()'''
driver.execute_script(js3)
sleep(3)
js4='''$("#submit").click()'''
driver.execute_script(js4)
sleep(3)


# driver.get("https://www.12306.cn/index/")
# sleep(2)
# driver.find_element_by_partial_link_text("往返").click()
# sleep(2)
# js1 = ''' $("#go_date").removeAttr("readonly");
#             $("#go_date").val("2020-04-09");
#           '''
# driver.execute_script(js1)
# sleep(2)




driver.get("http://127.0.0.1:82/zentao/project-create.html")
sleep(2)
js3 = '''document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML =111'''

driver.execute_script(js3)
sleep(2)

driver.quit()







