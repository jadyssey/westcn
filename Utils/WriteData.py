# coding: utf-8
"""
文件数据写入
"""

import xlwings as xw


# 将list数组写入Excel表格，SHEET_NUMBER为传入第几个sheet，A_Row为从第几行开始写入
def toExcel(listData, Excel_Path, SHEET_NUMBER=0, A_Row='a1', SAVE_PATH=None):
    print("=======你即将写入的数据为：=======")
    print(listData)
    print("=============================")

    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(Excel_Path)
    wb.sheets[SHEET_NUMBER].range(A_Row).expand('table').value = listData
    wb.save(SAVE_PATH)
    wb.close()
    app.quit()
