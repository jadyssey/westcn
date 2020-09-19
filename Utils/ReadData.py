# coding: utf-8
"""
文件数据读取
"""
import xlwings as xw


def readExcel(Excel_Path):
    app = xw.App(visible=False, add_book=False)
    # 新建工作簿 wb = app.books.add()
    wb = app.books.open(Excel_Path)
    # 引用工作表
    sht = wb.sheets[0]
    # 读取所有的值
    listExcel = sht.range('A1').expand().value
    # print("=============从Excel读取到的数据量为：=============")
    # print(len(listExcel))
    wb.save()
    wb.close()
    app.quit()
    return listExcel
