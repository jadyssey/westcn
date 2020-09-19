# 配置文件
import glob

# 动态获取hromedriver的位置
# CHROME_DRIVER = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
CHROME_DRIVER = glob.glob(r'C:\*\Google\Chrome\Application\chromedriver.exe')

All_Data_Path="D:/RPA/"

URL = "https://www.west.cn/services/yuding/?mode=chngrab"

File_full_XPath="/html/body/div[4]/div[2]/a[1]"
