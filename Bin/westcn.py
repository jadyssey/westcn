# coding: utf-8
"""
主程序
"""

from Config import *
from Utils.DownFile import downWestCn
from Utils.ReadData import readExcel


# ====程序入口====================================================================

if __name__ == '__main__':
    # 从网站上下载
    # filePath = downWestCn(URL, All_Data_Path,CHROME_DRIVER,File_full_XPath)
    # 读取文件数据
    listExcel = readExcel("D:\RPA\exp_2020_09_20_2897b3.csv")




