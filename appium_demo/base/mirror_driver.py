#coding:utf-8
from appium import webdriver
from util.write_user_command import WriteUserCommand
import time

class MirrorDriver:
    def __init__(self, i):
        self.driver = self.mirror_driver(i)

    def mirror_driver(self, i):
        print "This is mirror_driver", i
        wr = WriteUserCommand()
        device = wr.get_value('user_info_' + str(i), 'deviceName')
        port = wr.get_value('user_info_' + str(i), 'port')
        if device and port:
            desired_caps = {
                'platformName': 'Android',
                'deviceName': device,
                'app': 'E:\\05-平衡秤\\apk\\Small_release_v1.3.223-20190301.apk',
                'noReset': True,  # 不用每次都重新安装apk
                # 'newCommandTimeout': 120  # 自定义超时时间,超过此时间没有数据传输，将断开连接
            }
            driver = webdriver.Remote('http://127.0.0.1:' + str(port) + '/wd/hub', desired_caps)
            return driver
    
    # 进入主界面
    def main_interface(self):
        main_id = "com.ovation.healthmirror:drawable/face_tongue_layout_bg"
        self.driver.find_element_by_id(main_id).click()
        time.sleep(5)

    # 拍照
    def go_take_photos(self,face_or_tongue):
        face_id = "com.ovation.healthmirror:id/step_face"
        tongue_id = "com.ovation.healthmirror:id/step_tongue"
        photo_id = "com.ovation.healthmirror:id/take_picture"
        if face_or_tongue == 'tongue':
            self.driver.find_element_by_id(tongue_id).click()
        else:
            self.driver.find_element_by_id(face_id).click()
        time.sleep(5)
        self.driver.find_element_by_id(photo_id).click()

    # 分析图片
    def analyze_photo(self):
        id = "com.ovation.healthmirror:id/upload_btn"
        self.driver.find_element_by_id(id).click()

if __name__ == "__main__":
    mirror = MirrorDriver(0)




