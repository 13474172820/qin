import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import time
from selenium import webdriver
test_case=r'C:\Users\asus\PycharmProjects\Test-wang\KJ\test_case\\'
discover=unittest.defaultTestLoader.discover(test_case,pattern='test_*.py')
now=time.strftime('%Y-%m-%d %H-%M-%S')
rpath=r'C:\Users\asus\PycharmProjects\Test-wang\KJ\report\test_report.html'
fb=open(rpath,'wb')
run=HTMLTestRunner(stream=fb,title='自动化测试框架',description='溯源测试报告',tester='Tay')
run.run(discover)