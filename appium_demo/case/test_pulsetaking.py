# coding:utf-8
from appium import webdriver
import time

desired_caps = {
    'platformName':'Android',
    'deviceName':'4d98c4f6',
    # 'platformVersion':'4.4.4',
    'appPackage':'com.ovation.pulsetaking',
    # 查看当前app的Activity: adb shell "dumpsys window | grep mCurrent"
    # 'appActivity':'com.baidu.yuedu.base.ui.MainActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(5)
# 休眠5秒等待页面加载
time.sleep(5)
# driver.find_element_by_name("取消").click()
# time.sleep(2)
# driver.find_element_by_name("我的").click()


