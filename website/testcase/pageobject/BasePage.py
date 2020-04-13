__author__ = 'Administrator'

class Page():

    def __init__(self,driver):
        self.driver = driver
        self.base_url="http://localhost:8888"
        self.timeout=20

    def __open(self,url):
        print(self.base_url+url)
        self.driver.get(self.base_url+url)
        self.driver.maximize_window()
        assert self.driver.current_url == self.base_url+url, 'Did ont land on %s' % url

    def open(self):
        self.__open(self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)