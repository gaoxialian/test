__author__ = 'Administrator'
from selenium import webdriver
import time
from chandao.common.base import Base
from time import sleep

class AddBugPage(Base):

    loc_test = ('link text', '测试')
    loc_bug = ('link text', 'Bug')
    loc_add_bug = ('xpath', "//*[@id='createActionMenu']/a")
    loc_truc = ('xpath', "//*[@id='openedBuild_chosen']/ul")
    loc_truc_add = ('xpath', "//*[@id='openedBuild_chosen']/div/ul/li")
    loc_title = ('id', "title")

    # 富文本框
    loc_iframe = ('css selector', ".ke-edit-iframe")
    loc_input_body = ('css selector', ".article-content")
    loc_save = ('id', "submit")

    loc_new_bug_list = ('xpath', "//*[@id='bugList']/tbody/tr/td[4]/a")

    ''' 新增bug成功 '''
    def add_bug(self, _title, _body):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_add_bug)
        self.click(self.loc_truc)
        self.click(self.loc_truc_add)
        self.sendKeys(self.loc_title, _title)
        # body
        ele = self.findElement(self.loc_iframe)
        self.driver.switch_to.frame(ele)
        self.sendKeys(self.loc_input_body, _body)
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

    def is_add_bug_success(self, _text):
        return self.is_text_in_element(self.loc_new_bug_list, _text)





