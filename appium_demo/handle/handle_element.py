#coding=utf-8
from page.login_page import LoginPage

class HandleElement:
    '''
    操作登录页面上各元素
    '''
    def __init__(self, i):
        self.login_page = LoginPage(i)

    def send_user(self, user):
        '''
        输入用户名
        '''
        self.login_page.get_username_element().send_keys(user)

    def send_pwd(self, pwd):
        '''
        输入密码
        '''
        self.login_page.get_password_element().send_keys(pwd)

    def click_login(self):
        '''
        点击登录按钮
        '''
        self.login_page.get_login_button_element().click()

    def click_forget_login(self):
        '''
        点击忘记密码
        '''
        self.login_page.get_forget_passwd_element().click()

    def click_register(self):
        '''
        点击注册
        '''
        self.login_page.get_register_element().click()

    def get_tost_result(self, message):
        '''
        获取tost，根据结果返回数据
        '''
        tost_element = self.login_page.get_tost_element(message)
        if tost_element:  # 如果找到tost元素
            return True
        else:
            return False



