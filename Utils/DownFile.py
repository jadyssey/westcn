# coding: utf-8
"""
文件下载功能
"""

import urllib.request
from selenium import webdriver
import glob


# for name in glob.glob('D:\*\exp_2020_09_*.csv'):
#     print (name)

def downWestCn(URL, All_Data_Path):
    for CHROME_DRIVER in glob.glob('C:\*\Google\Chrome\Application\chromedriver.exe'):
        print(CHROME_DRIVER)

    browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
    browser.get(URL)

    fileUrl = browser.find_element_by_xpath("/html/body/div[4]/div[2]/a[1]").get_attribute("href")
    fileName = All_Data_Path + fileUrl.split('/')[-1]
    print("保存文件的路径", fileName)
    urllib.request.urlretrieve(fileUrl, filename=fileName)

    # # 退出
    browser.close()
    browser.quit()
