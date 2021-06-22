#coding=utf-8
# Date:2021-6-16
# Auther:wang
# 模块：产品管理模块
import select
from selenium import webdriver
import time
from KJ.common.log_in import Log_in
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from ddt import ddt,data,unpack
from KJ.Test_date.read_add import *

@ddt
class Test_cpgl(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl = Log_in()
        self.dl.log_in()

    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    @data(*Add().read_data())
    @unpack
    def test1_add_product1(self,m1,m2,m3,m4,m5,m6,m7,m8,q,w,e,r):
        self.dl.web.find_element_by_xpath(m1).click()
        self.dl.web.find_element_by_xpath(m2).click()
        self.dl.web.find_element_by_xpath(m3).send_keys(q)
        self.dl.web.find_element_by_xpath(m4).send_keys(w)
        self.dl.web.find_element_by_xpath(m5).send_keys(e)
        self.dl.web.find_element_by_xpath(m6).send_keys(r)
        self.dl.web.find_element_by_xpath(m7).click()
        self.assertIn('产品新增成功！', self.dl.web.find_element_by_xpath(m8).text, msg='失败')
"""
    def test2_add_product2(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('土豆豆')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('1231231623')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('456456456')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys("小土豆")
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[9]/div/button').click()
        self.assertIn('产品编号有重复', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='失败')

    def test3_add_product3(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('土豆')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('12389101112')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('124564566456')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys("小土豆")
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[9]/div/button').click()
        self.assertIn('产品条码有重复!', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='失败')

    def test4_change(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[1]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div[2]/div/section/div/form/div[1]/div[1]/input').send_keys('土马铃薯')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div[2]/div/section/div/form/div[2]/div[1]/input').send_keys('00000009')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div[1]/input').send_keys('000000010')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys('马铃薯002')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button').click()
        self.assertIn('产品更新成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test5_delete_one(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span').click()
        self.dl.web.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        self.assertIn('产品删除成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='失败')

    def test6_delete_many(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chkAll"]').click()
        self.dl.web.find_element_by_xpath('//*[@id="del"]').click()
        a=self.dl.web.switch_to.alert
        a.accept()
        time.sleep(3)
        b=self.dl.web.switch_to.alert
        self.assertIn('删除成功',b.text, msg='失败')
        b.accept()
"""


if __name__ == '__main__':
    unittest.main()
#     suites=unittest.TestSuite()
#     suites.addTest(Test_cpgl('test_add_product1'))
#     suites.addTest(Test_cpgl('test_add_product2'))
#     suites.addTest(Test_cpgl('test_add_product3'))
#     suites.addTest(Test_cpgl('test_delete_one'))
#     rpath=r'C:\Users\asus\PycharmProjects\Test-wang\KJ\report\test_report.html'
#     fb=open(rpath,'wb')
#     run=HTMLTestRunner(stream=fb,title='自动化测试框架',description='溯源测试报告',tester='Tay')
#     # run=unittest.TextTestRunner()
#     run.run(suites)