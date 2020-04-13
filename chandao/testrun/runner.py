__author__ = 'Administrator'
from chandao.testrun import HTMLTestRunner_cn
import sys
import unittest
import os
project_dir = r"C:\Users\Administrator\PycharmProjects\test"
sys.path.append(project_dir)

test_dir = "../testcase"
test_report = "../testreport"

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

reoprt_path = os.path.join(test_report, "report.html")
with open(reoprt_path, 'wb') as file:
    run = HTMLTestRunner_cn.HTMLTestRunner(stream=file, title="title",description="描述", save_last_try=2)
    run.run(discover)
