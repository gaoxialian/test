__author__ = 'Administrator'
import HTMLTestRunner_cn
import sys
import time
import unittest
import os
project_dir = "C:\\Users\\Administrator\\PycharmProjects\\test"
sys.path.append(project_dir)

test_dir =os.path.join(project_dir,'chandao', 'testcases')
test_report = os.path.join(project_dir,'chandao', 'testreport')

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

reoprt_path = os.path.join(test_report, "report.html")
with open(reoprt_path, 'wb') as file:
    run = HTMLTestRunner_cn.HTMLTestRunner(stream=file, title="title",description="描述",retry =2)
    run.run(discover)
