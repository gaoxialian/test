__author__ = 'Administrator'
from selenium.webdriver.support import expected_conditions as EC

class hello():

    def __init__(self, a):
        print(a)

    def __call__(self, b):
        print(b)

if __name__ == '__main__':
    h = hello("1211")
    h("222")