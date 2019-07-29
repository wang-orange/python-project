# coding:utf-8
import os
from appium import webdriver

'''
abspath()与realpath()区别：
os.path.abspath: returns the absolute path, but does NOT resolve symlinks.
os.path.realpath: will first resolve any symbolic links in the path, and then return the absolute path.
比如目录下有两个文件a,b,但b其实a的链接
$ ls -l
total 0
-rw-rw-r-- 1 guest guest 0 Jun 16 08:36 a
lrwxrwxrwx 1 guest guest 1 Jun 16 08:36 b -> a

>>> from os.path import abspath, realpath
>>> abspath('b')
'/home/guest/play/paths/b'
>>> realpath('b')
'/home/guest/play/paths/a'
'''

# 获取项目的根目录路径
# abspath("") 参数为空，则返回当前文件所在目录的绝对路径
dir_path = os.path.dirname(os.path.abspath("")).decode('gbk')  # 如果路径存在中文，需要decode('gbk')
print  dir_path
# 获取apk路径
def appPath(app_name):
    return os.path.join(dir_path,"app",app_name)
# 用lambda 函数更简洁
app_path = lambda app_name:os.path.join(dir_path,"app",app_name)

desired_caps = {
    'platformName':'Android',
    'deviceName':'b8bc1bd6615b',
    'platformVersion':'4.4.4',
    'app':appPath('baiduyuedu_5891.apk'),
    'appPackage':'com.baidu.yuedu',
    'appActivity':'com.baidu.yuedu.splash.SplashActivity',
    'noReset':'true'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

# if __name__ == '__main__':
#     print appPath("baidu.apk")
#     print app_path("baidu.apk")