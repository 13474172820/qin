#coding=utf-8
# Date:2021-6-16
# Auther:wang
# 模块：发货管理模块
from selenium import webdriver
import time
from KJ.common.log_in import Log_in
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
class Test_FHGL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl=Log_in()
        self.dl.log_in()
        self.dl.web.implicitly_wait(20)
    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    def test0_add_product(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[1]/a','/html/body/section/aside/div/ul/li[1]/ul/li[1]/a'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input'],['红烧牛肉干','0203050602321','986532147852'])
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys('lalalla')
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[9]/div/button'])
        # self.assertIn('产品新增成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='失败')

    def test1_add_wuliuma_one(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[2]/a/span[1]','/html/body/section/aside/div/ul/li[2]/ul/li[2]/a'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input','/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input'],['222222222222222','Tay100000000000','612430612430'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/div[2]/input'],['红烧牛肉干'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/div/div[2]/div/div[2]/div[1]','/html/body/section/section/section/div/div/section/div/form/div[5]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[5]/div[1]/div/div[2]/input'],['王二小'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[5]/div[1]/div/div[2]/div/div[2]/div[2]'])
        s66=Select(self.dl.web.find_element_by_xpath('//*[@id="qiyong"]'))
        s66.select_by_index(0)
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[7]/div/button'])
        # self.assertIn('恭喜，成功生成一个防伪码！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test1_send_one(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[6]/a/span[1]','/html/body/section/aside/div/ul/li[6]/ul/li[1]/a','/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/div[2]/input'],['红烧牛肉干'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]','/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/div/div[2]/input'],['王二小'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[3]'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/textarea'],['612430612430'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/div[5]/div/button'])
        self.assertIn('发货成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')


    def test_7_deleteWLM(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[2]/a/span[1]','/html/body/section/aside/div/ul/li[2]/ul/li[4]/a','/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/input'],['222222222222222'])
        self.dl.click(['/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[1]','/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div/button'])
        # self.assertIn('222222222222222批次所属防伪码批量删除成功', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test8_delete_addone(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[1]/a/span[1]','/html/body/section/aside/div/ul/li[1]/ul/li[2]/a'])
        self.dl.send_keys(['/html/body/section/section/section/div/div/section/div/form/div[1]/input'],['红烧牛肉干'])
        self.dl.click(['/html/body/section/section/section/div/div/section/div/form/button','//*[@id="chk[]"]','/html/body/section/section/section/form/div/div/section/table/tbody/tr/td[8]/span','/html/body/div[4]/div[3]/a[1]'])
        # self.assertIn('产品删除成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')