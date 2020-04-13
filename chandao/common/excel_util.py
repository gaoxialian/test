__author__ = 'Administrator'
import xlrd
import os
class ExcelUtil():

    def __init__(self, filepath, sheetName='Sheet1'):
        self.data = xlrd.open_workbook(filepath)
        self.table = self.data.sheet_by_name(sheetName)
        self.rows = self.table.nrows
        self.cols = self.table.ncols
        self.keys = self.table.row_values(0)

    def dict_data(self):
        if self.rows <= 1:
            print("总行数少于1")
        else:
            result = []
            for row in range(self.rows -1):
                s = {}
                value = self.table.row_values(row+1)
                for col in range(self.cols):
                    s[self.keys[col]] =value[col]
                result.append(s)
        return result

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(base_dir,'data', 'users.xlsx')
    excel = ExcelUtil(filepath)
    print(excel.dict_data())