#coding=utf-8
from util.get_by_location import GetByLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver

class LoginPage:
    '''
    获取登录页面所有的元素信息
    '''
    def __init__(self, i):  # 进入登录界面
        base_driver = BaseDriver(i)
        login_driver = base_driver.go_login()
        # self.driver = base_driver.android_driver(i)
        self.get_by_location = GetByLocation(login_driver)

    def get_username_element(self):
        '''
        用户名元素
        '''
        return self.get_by_location.get_element('username')

    def get_password_element(self):
        '''
        密码元素
        '''
        return self.get_by_location.get_element('password')

    def get_login_button_element(self):
        '''
        登录按钮元素
        '''
        return self.get_by_location.get_element('login_button')

    def get_forget_passwd_element(self):
        '''
        忘记密码元素
        '''
        return self.get_by_location.get_element('forget_pwd')

    def get_register_element(self):
        '''
        注册元素
        '''
        return self.get_by_location.get_element('register')

    def get_tost_element(self, message):
        '''
        tost_element
        '''
        tost_element = ('xpath', '//*[contains(@text, '+message+')]')
        return WebDriverWait(self.get_by_location.login_driver, 20, 0.1).until(EC.presence_of_element_located(tost_element))

if __name__ == '__main__':
    login = LoginPage(0)
    # login.get_username_element()
    time.sleep(10)
    login.get_tost_element('登录密码错误')
