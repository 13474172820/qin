#coding=utf-8
# Date:2021-6-16
# Auther:wang
# 模块：溯源管理模块
from selenium import webdriver
import time
from KJ.common.log_in import Log_in
import unittest
from selenium.webdriver.support.select import Select
class Test_SYGL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl=Log_in()
        self.dl.log_in()
        self.dl.web.implicitly_wait(20)
    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    def test1_add(self):
        list_d=['/html/body/section/aside/div/ul/li[4]/a/span[1]','/html/body/section/aside/div/ul/li[4]/ul/li[1]/a']
        self.dl.click(list_d)
        list_ard =['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input']
        list_sh=['大家好',]
        self.dl.send_keys(list_ard,list_sh)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div/div/div[2]/iframe').send_keys('lalalalalalla')
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[3]/div/button'])
        self.assertIn('恭喜，溯源增加成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test2_look(self):
        list_d=['/html/body/section/aside/div/ul/li[4]/a/span[1]','/html/body/section/aside/div/ul/li[4]/ul/li[2]/a']
        self.dl.click(list_d)
        self.dl.send_keys(['//*[@id="key"]'],['大家好'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/button'])
        self.assertIn('大家好',self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[3]/b').text,msg='失败')

    def test3_change(self):
        list_d = ['/html/body/section/aside/div/ul/li[4]/a/span[1]', '/html/body/section/aside/div/ul/li[4]/ul/li[2]/a','//*[@id="chk[]"]','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/a']
        self.dl.click(list_d)
        self.dl.send_keys(['/html/body/section/section/section/div[2]/div/section/div/form/div[1]/div[1]/input'],['北京老冰棍棍'])
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div/div/div[2]/iframe').send_keys('大秦帝国')
        self.dl.click(['/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div/button'])
        self.assertIn('溯源更新成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test4_delete_one(self):
        list_d = ['/html/body/section/aside/div/ul/li[4]/a/span[1]', '/html/body/section/aside/div/ul/li[4]/ul/li[2]/a','//*[@id="chk[]"]','/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[5]/span','/html/body/div[4]/div[3]/a[1]']
        self.dl.click(list_d)
        self.assertIn('删除成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test5_delete_many(self):
        list_d = ['/html/body/section/aside/div/ul/li[4]/a/span[1]', '/html/body/section/aside/div/ul/li[4]/ul/li[2]/a','//*[@id="chkAll"]','//*[@id="del"]',]
        self.dl.click(list_d)
        m=self.dl.web.switch_to.alert
        m.accept()
        time.sleep(3)
        n=self.dl.web.switch_to.alert
        self.assertIn('批量删除成功',n.text, msg='失败')
        n.accept()

# if __name__ == '__main__':
#     unittest.main()
