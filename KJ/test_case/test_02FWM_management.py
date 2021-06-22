#coding=utf-8
# Date:2021-6-16
# Auther:wang
# 模块：防伪码管理
from selenium import webdriver
import time
from KJ.common.log_in import Log_in
import unittest
import pyautogui
from selenium.webdriver.support.select import Select
class Test_FWMGL(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dl=Log_in()
        self.dl.log_in()
    @classmethod
    def tearDownClass(self):
        self.dl.web.close()
        self.dl.web.quit()

    def test0_add_product1(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('99999红烧牛肉干')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('1231231623')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('124564566456')
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[8]/div/div/div[2]/iframe').send_keys("小小小肉干")
        self.dl.web.find_element_by_xpath(
            '/html/body/section/section/section/div/div/section/div/form/div[9]/div/button').click()
        self.assertIn('产品新增成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='失败')

    def test1_increaseFWM_many(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[1]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('8888888888')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('10')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('Tay')
        s1=Select(self.dl.web.find_element_by_xpath('//*[@id="code_type"]'))
        s1.select_by_index(2)
        s2=Select(self.dl.web.find_element_by_xpath('//*[@id="txm_type"]'))
        s2.select_by_index(0)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[5]/div[2]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[5]/div[2]/input').send_keys('6')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[6]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[6]/div[1]/input').send_keys('50')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div[1]/div/div[1]')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[8]/div[1]/div/div[1]')
        s5=Select(self.dl.web.find_element_by_xpath('//*[@id="qiyong"]'))
        s5.select_by_index(0)
        self.dl.web.find_element_by_xpath('//*[@id="tj"]').click()
        self.assertIn('恭喜，已成功生成50个防伪码！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test2_increaseFWM_one(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('9999999999')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('Tay1995061')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('9999999999999')
        s9=Select(self.dl.web.find_element_by_xpath('//*[@id="qiyong"]'))
        s9.select_by_index(0)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
        self.assertIn('恭喜，成功生成一个防伪码！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')


    def test3_increaseFWM_one_cover(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input').send_keys('20210609')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[2]/div[1]/input').send_keys('Tay1995061')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').clear()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[3]/div[1]/input').send_keys('0000000001')
        s9=Select(self.dl.web.find_element_by_xpath('//*[@id="qiyong"]'))
        s9.select_by_index(0)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div/div/section/div/form/div[7]/div/button').click()
        self.assertIn('防伪码有重复！!',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test4_changeFWM(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[3]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="txm"]').send_keys('0000000001')
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[1]').click()
        self.dl.send_keys(['/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[2]/input'],['红烧牛肉干'])
        self.dl.click(['/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div','/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/div[2]/input'],['王二小'])
        self.dl.click(['/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[8]','/html/body/section/section/section/div[1]/div/section/div/form/div[4]/div/button'])
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div[1]/div/div[2]/div/div[2]/div[3]').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/span').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[3]').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[4]/div/button').click()
        self.assertIn('批量修改成功',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test5_changeFWMZT(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[5]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="txm"]').send_keys('0000000001')
        s11=Select(self.dl.web.find_element_by_xpath('//*[@id="qiyong"]'))
        s11.select_by_index(1)
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div/button').click()
        self.assertIn('操作成功！',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def Ttest6_daochuFWM(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[7]/a').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div/div').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div/div/div[2]/div/div[2]/div[1]').click()
        s12=Select(self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[3]/div/select'))
        s12.select_by_index(1)
        s13 = Select(self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[4]/div/select'))
        s13.select_by_index(1)
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[5]/div/button').click()
        self.dl.click(['/html/body/section/section/section/div[1]/div/section/div/form/div[5]/div/button'])
        windows = self.dl.web.window_handles
        self.dl.web.switch_to.window(windows[-1])
        self.dl.click(['/html/body/div[1]/div/a[1]/span/b'])
        self.dl.web.maximize_window()
        pyautogui.moveTo(589,458)
        pyautogui.click()
        pyautogui.moveTo(844,539)
        pyautogui.click()

    def test7_delete(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[2]/a/span[1]','/html/body/section/aside/div/ul/li[2]/ul/li[4]/a','/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/input'],['8888888888'])
        self.dl.click(['/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[2]','/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div/button'])
        self.assertIn('8888888888批次所属防伪码批量删除成功',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test8_delete1(self):
        self.dl.click(['/html/body/section/aside/div/ul/li[2]/a/span[1]','/html/body/section/aside/div/ul/li[2]/ul/li[4]/a','/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[1]'])
        self.dl.send_keys(['/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/input'],['9999999999'])
        self.dl.click(['/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[1]','/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div/button'])
        self.assertIn('9999999999批次所属防伪码批量删除成功', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')

    def test9_delete_one(self):
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/a/span[1]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[1]/ul/li[2]/a').click()
        self.dl.web.find_element_by_xpath('//*[@id="chk[]"]').click()
        self.dl.web.find_element_by_xpath('/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span').click()
        self.dl.web.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]').click()
        self.assertIn('产品删除成功！', self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text, msg='失败')



    # def test7_deleteFWM(self):
        # self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/a/span[1]').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/aside/div/ul/li[2]/ul/li[4]/a').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[1]/div[1]/div/div[2]/div/div[2]/div[1]').click()
        # self.dl.web.find_element_by_xpath('/html/body/section/section/section/div[1]/div/section/div/form/div[2]/div/button').click()
        # self.assertIn('批次所属防伪码批量删除成功',self.dl.web.find_element_by_xpath('/html/body/div[3]/div').text,msg='失败')



# if __name__ == '__main__':
#     unittest.main()

