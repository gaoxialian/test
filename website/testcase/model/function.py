__author__ = 'Administrator'
from driver import *
import os
import smtplib
from email.mime.text import MIMEText
from email.header  import Header

def save_image(driver, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_dir, "testreport/screenshot",filename)
    driver.get_screenshot_as_file(file_path)

#查找最新的测试报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    # print("the latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file

#将测试报告发送到邮件
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = 'gaoxialian_cmss@163.com'
    password = 'SFWAPUOKXPRVZXJJ'

    sender = 'gaoxialian_cmss@163.com'
    receives = ['y15050193776@139.com', 'y1253555947@qq.com']

    subject = 'Web Selenium 自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")

if __name__ == '__main__':
    driver = browser()
    save_image(driver, "11.png")
    driver.quit()
