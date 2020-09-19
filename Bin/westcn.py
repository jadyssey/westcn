# coding: utf-8
"""
主程序
"""

from Config import *
from Utils.DownFile import downWestCn
from Utils.ReadData import readExcel
import re


def filterData(list):
    # 判断是否包含数字
    pattern = re.compile('[0-9]+')

    listData = []
    for i in range(1, len(list)):
        com = list[i][2]
        amount = list[i][1]
        noNumber = list[i][0]
        match = pattern.findall(noNumber)

        if com == "com" and amount == 4 and len(match) == 0:
            # print(com, amount, noNumber, match)
            listData[i] = com
    return listData

# ====程序入口====================================================================

if __name__ == '__main__':
    # 从网站上下载
    # filePath = downWestCn(URL, All_Data_Path,CHROME_DRIVER,File_full_XPath)
    # 读取文件数据
    listExcel = readExcel("D:\RPA\exp_2020_09_23_21d704.csv")

    # 筛选数据
    listData = filterData(listExcel)
