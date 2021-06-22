import xlrd
from ddt import ddt
class Add():
    def read_data(self):
        self.reselt=[]
        self.data=xlrd.open_workbook(r'C:\Users\asus\Desktop\add.xls')
        table=self.data.sheet_by_index(0)
        for i in range(1,table.ncols):
            self.reselt.append(table.col_values(i))
        return self.reselt
# print(Add().read_data())
# P=Add()
# print(P.read_data())