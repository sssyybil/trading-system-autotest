"""
@Author SunYL
@Time 2023/9/12 22:28
"""

from selenium import webdriver
from selenium.webdriver.chrome import service

from common.tools import get_project_path, sep

from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")  # 设置窗口大小，设置为 1920*1080
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 去除 “chrome 正在受到自动测试软件的控制” 的提醒
options.add_argument("--ignore-certificate-errors")  # 忽略网站的证书认证错误，解决 Selenium 无法访问 https 的问题
options.add_argument("--allow-insecure-localhost")  # 忽略 localhost 上的 TLS/SSL 错误
options.add_argument("--incognito")  # 设置为无痕模式
# options.add_argument("--headless")  # 设置为无头模式，即不显示打开浏览器窗口，整个流程都在后台执行
options.add_argument("--disable-gpu")  # 禁用 GPU 的页面加速，解决卡顿
options.add_argument("--no-sandbox")  # 禁用沙箱，解决卡顿
options.add_argument("--disable-dev-shm-usage")  # 解决卡顿

driver = webdriver.Chrome(
    service=service.Service(
        executable_path=get_project_path() + sep(["driver_files", "chromedriver"], add_sep_before=True)),
    options=options)

driver.get("http://192.168.56.20")
sleep(5)
driver.quit()
