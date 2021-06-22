#coding=utf-8
# Date:2021-6-16
# Auther:wang
# 模块：流程管理模块
from selenium import webdriver
import time
from KJ.common.log_in import Log_in
import unittest
from selenium.webdriver.support.select import Select
class Test_LCGL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl=Log_in()
        self.dl.log_in()

    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    def test1_add(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('出库')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('0021')
        s13=Select(self.dl.web.find_element_by_xpath('//*[@id="zt"]'))
        s13.select_by_index(1)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        self.assertIn('操作成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test2_add1(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('出库')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('201')
        s13=Select(self.dl.web.find_element_by_xpath('//*[@id="zt"]'))
        s13.select_by_index(1)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        self.assertIn('流程类别名有重复!',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test3_change(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('米老鼠大战汤姆猫')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('010')
        s15=Select(self.dl.web.find_element_by_xpath('//*[@id="zt"]'))
        s15.select_by_index(0)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div/button').click()
        self.assertIn('更新成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test4_delete_one(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[7]/span').click()
        self.dl.web.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        self.assertIn('删除成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test5_delete_many(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chkAll"]').click()
        self.dl.web.find_element_by_xpath('//*[@id="del"]').click()
        a = self.dl.web.switch_to.alert
        a.accept()
        time.sleep(3)
        a1=self.dl.web.switch_to.alert
        self.assertIn('批量删除成功',a1.text, msg='失败')
        a1.dismiss()


    def test6_sousuo(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div/input').send_keys('发货')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/button').click()
        self.assertIn('发货',self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[3]').text,msg='失败')

    def test7_add_LCJL(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[3]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[5]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/textarea').send_keys('17772355')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/input').send_keys('张三')
        self.dl.web.find_element_by_xpath('//*[@id="czdate"]').clear()
        self.dl.web.find_element_by_xpath('//*[@id="czdate"]').send_keys('2021-8-9')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[6]/div/button').click()
        self.assertIn('操作成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test8_change(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/span').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[6]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('63395943')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[4]/div[1]/input').send_keys('李四四')
        s20=Select(self.dl.web.find_element_by_xpath('//*[@id="zt"]'))
        s20.select_by_index(0)
        self.dl.web.find_element_by_xpath('//*[@id="czdate"]').clear()
        self.dl.web.find_element_by_xpath('//*[@id="czdate"]').send_keys('2021-9-8')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
        self.assertIn('更新成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    # def test9_delete_one(self):
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/a/span[1]').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[3]/ul/li[4]/a').click()
    #     self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
    #     self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span').click()
