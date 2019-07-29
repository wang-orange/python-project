# coding:utf-8

from appium import webdriver
import time
import unittest

'''
# **************************************************
# 查看当前app的Activity: adb shell "dumpsys window | grep mCurrent"
# activity在清单文件里面没添加android:exported=”true”，将不能直接打开对应的activity(会报错 Error: Permission to start activity denied.)，需要从启动页activity打开。
# exported属性就是设置是否允许activity被其它程序调用
# **************************************************
# 'platformVersion':'5.1.1',
# 老版本的Appium需要用到以下两项：
# 'appPackage':'com.ovation.healthmirror',  # 老版本的Appium需要用到
# 'appActivity':'com.ovation.healthmirror.HealthMirrorMainActivity'  # HealthToolsActivity  HealthMirrorMainActivity
# ***************************************************
'''

class TestSkin:
    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'P1QRM974FV',
            'app': 'E:\\04-mini健康镜\\皮肤检测\\Small_release_v1.3.215-20181010.apk',
            'noRest': 'true'
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver


    def get_size(self):
        size = self.driver.get_window_size()
        print size
        return size

    def swipe_left(self):
        size = self.get_size()
        width = size['width']
        height = size['height']
        x1 = width / 10 * 9
        x2 = width / 10
        x = width / 2
        y = height / 2
        self.driver.swipe(x + 280, y, x, y)

    def find_my_element(self, element):
        count = 0  
        flag = False  # 找到该元素后置为True
        while count<15:
            try:
                elt = self.driver.find_element_by_id(element)
            except Exception:
                print "NoSuchElementError"
                time.sleep(1)
                count = count + 1
            else:
                flag = True
                while True:
                    elt.click()
                    try:
                        self.driver.find_element_by_id(element)  # 点击按钮后没有进入下个界面时，等待1秒后再点击，否则跳出循环
                    except Exception:
                        break
                    else:
                        time.sleep(1)
                return flag
                break

    def go_skin(self):
        skin_icon = "com.ovation.healthmirror:id/skin_icon_image_view"
        home_icon = "com.ovation.healthmirror:id/skin_home_image"
        take_picture = "com.ovation.healthmirror:id/take_picture"
        upload_picture = "com.ovation.healthmirror:id/upload_picture_button"
        load = "com.ovation.healthmirror:id/dialog_text"
        self.find_my_element(skin_icon)  # 点击皮肤检测
        print "进入皮肤检测"

        while True:
            flag = self.find_my_element(take_picture)  # 拍照
            if flag:
                print "拍照结束"
                self.find_my_element(upload_picture)  # 分析图像
                print "分析结束"
                time.sleep(20)
            else:
                self.find_my_element(home_icon)
                break


if __name__ == "__main__":
    skin = TestSkin()
    # driver.implicitly_wait(15)  # 报错，待查
    # time.sleep(5)
    skin.swipe_left()
    time.sleep(2)
    skin.swipe_left()
    time.sleep(2)
    elements = skin.driver.find_elements_by_class_name("android.widget.ImageView")
    print len(elements)
    elements[1].click()  # 进入“视觉生活”
    time.sleep(2)

    for i in range(10):
        print "test---->%s"%i
        skin.go_skin()


