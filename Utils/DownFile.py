# coding: utf-8
"""
文件下载功能
"""

import urllib.request
from selenium import webdriver


def downWestCn(URL, All_Data_Path,CHROME_DRIVER,File_full_XPath):

    # for name in glob.glob('D:\*\exp_2020_09_*.csv'):
    #     print (name)
    # 打开需要下载文件的网址
    browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
    browser.get(URL)

    # 通过full Xpath 定位到文件的URL中
    fileUrl = browser.find_element_by_xpath(File_full_XPath).get_attribute("href")
    fileName = fileUrl.split('/')[-1]
    filePath = All_Data_Path + "\\" + fileName
    # print("保存文件的路径", filePath)
    urllib.request.urlretrieve(fileUrl, filename=filePath)

    # # 退出
    browser.close()
    browser.quit()
    return filePath
