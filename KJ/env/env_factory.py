import yaml
import os
class Read_config():
    def __init__(self):
        # self.curPath=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # self.yaml1=os.path.join(self.curPath,'config\config.yaml')
        # self.f1=open(self.yaml1,'rb')
        # self.f1=open(r'C:\Users\asus\PycharmProjects\Test-wang\KJ\config\config.yaml','rb')  打开yaml文件
        with open(r'C:\Users\asus\PycharmProjects\Test-wang\KJ\config\config.yaml', 'rb') as self.f1:
            self.config_file=yaml.load(self.f1,Loader=yaml.FullLoader)  #导入yaml文件数据
            self.username=self.config_file['user']['username']  #根据变量组读取具体数据。
            self.password=self.config_file['user']['password']
            self.url=self.config_file['user']['url']
# a=Read_config()
# print(a.url)


