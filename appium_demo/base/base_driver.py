#coding=utf-8
from appium import webdriver
import time
from util.write_user_command import WriteUserCommand

class BaseDriver:
    def __init__(self, i):
        self.driver = self.android_driver(i)

    def android_driver(self, i):
        print "This is android_driver", i
        wr = WriteUserCommand()
        device = wr.get_value('user_info_'+str(i), 'deviceName')
        port = wr.get_value('user_info_'+str(i), 'port')
        desired_caps = {
            'platformName': 'Android',
            # 'automationName':'UiAutomator2',  # 测试平台，默认Appium，但定位tost元素必须用UiAutomator2，并且android版本必须5以上
            'deviceName': device,
            'app': 'F:\\AutoTest\\工具\\baiduyuedu_5891.apk',
            # 'appWaitActivity':'com.imooc.component.imoocmain.index.MCMainActivity',
            'noReset': True  # 不用每次都重新安装apk
        }
        driver = webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub', desired_caps)
        # driver.start_activity(' cn.com.open.mooc', 'cn.com.open.mooc.component.user.activity.login.MCLoginActivity')  # 切不过去？？
        return driver

    def go_login(self):
        '''
        进入登录页面
        '''
        time.sleep(4)
        element = self.driver.find_element('id', 'cn.com.open.mooc:id/tab_layout')  # 层级定位
        elements = element.find_elements_by_class_name("android.widget.RelativeLayout")
        elements[3].click()  # 点击“账号”
        print "进入注册界面"
        time.sleep(2)
        self.driver.find_element_by_id("cn.com.open.mooc:id/rl_login_before").click()
        # print "进入登录界面"
        # time.sleep(2)
        # self.driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login").click()
        return self.driver

if __name__ == "__main__":
    base = BaseDriver()
    # base.go_login()
