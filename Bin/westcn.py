# coding: utf-8
"""
主程序
"""
import re
from Config import *
from Utils.DownFile import downWestCn
from Utils.ReadData import readExcel
from Utils.WriteData import toExcel


def filterData(list):
    # 判断是否包含数字
    pattern = re.compile('[0-9]+')

    listData = []
    for i in range(1, len(list)):
        com = list[i][2]
        # 筛选4位数网址
        amount = list[i][1]
        noNumber = list[i][0]
        match = pattern.findall(noNumber)
        # 网址不包含 -
        str = '-'
        if amount == 4 and len(match) == 0 and str not in noNumber and (com == "com" or com == "me"):
            # print(com, amount, noNumber, match)
            listData.append(noNumber)
    return listData

# 一维数组转换为二位数组
def listChangeTwo(list):
    # print(len(list))
    listLen = int(len(list)/3)+1
    # print(listLen)
    listTwoData = []
    listTwoData.append(list[0:listLen])
    listTwoData.append(list[listLen:listLen*2])
    listTwoData.append(list[listLen*2:])
    if len(listTwoData[2]) < listLen:
        for i in range(0,listLen-len(listTwoData[2])):
            listTwoData[2].append("强迫症福音")
    # print(len(listTwoData[2]))
    return listTwoData
# ====程序入口====================================================================
if __name__ == '__main__':
    # 从网站上下载
    filePath = downWestCn(URL, All_Data_Path,CHROME_DRIVER,File_full_XPath)
    # 读取文件数据
    # listExcel = readExcel("D:\RPA\exp_2020_09_20_2897b3.csv")
    listExcel = readExcel(filePath)

    # 筛选数据
    listData = filterData(listExcel)
    # 一维数组转换为二位数组
    listTwoData= listChangeTwo(listData)

    # 将数据写入表格
    toExcel(listTwoData,SAVE_PATH=All_Data_Path+"\\output.xlsx")







