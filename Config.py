# 配置文件
import glob
from pathlib import Path


# 动态获取hromedriver的位置
# CHROME_DRIVER = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
CHROME_DRIVER = glob.glob(r'C:\*\Google\Chrome\Application\chromedriver.exe')

All_Data_Path = Path("D:/RPA/")
isOk = All_Data_Path.is_dir()
if not isOk:
    All_Data_Path.mkdir(exist_ok=True)
# 转成字符串类型
All_Data_Path=str(Path(All_Data_Path))

URL = "https://www.west.cn/services/yuding/?mode=chngrab"

File_full_XPath="/html/body/div[4]/div[2]/a[1]"
