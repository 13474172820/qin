import time
from selenium import webdriver
import requests
from KJ.env.env_factory import *
class Log_in():
    def log_in(self):
        self.web = webdriver.Firefox()
        self.web.implicitly_wait(20)
        self.web.get(Read_config().url)
        self.web.find_element_by_xpath('/html/body/div/section/form/div/input[1]').send_keys(Read_config().username)
        self.web.find_element_by_xpath('/html/body/div/section/form/div/input[2]').send_keys(Read_config().password)
        self.web.find_element_by_xpath('/html/body/div/section/form/div/input[3]').click()

    def send_keys(self,list_adr,list_sh):
        for p in range(len(list_adr)):
            self.web.find_element_by_xpath(list_adr[p]).clear()
            self.web.find_element_by_xpath(list_adr[p]).send_keys(list_sh[p])

    def click(self,list_d):
        for d in list_d:
            self.web.find_element_by_xpath(d).click()



# Log_in().log_in()

