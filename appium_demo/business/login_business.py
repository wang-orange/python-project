#coding=utf-8
from handle.handle_element import HandleElement

class LoginBusiness:
    def __init__(self, i):
        self.login_handle = HandleElement(i)

    def login_success(self):
        self.login_handle.send_user("18600407736")
        self.login_handle.send_pwd("orange0419")
        self.login_handle.click_login()

    def login_user_error(self):
        self.login_handle.send_user("18600407733")
        self.login_handle.send_pwd("orange")
        self.login_handle.click_login()
        login_flag = self.login_handle.get_tost_result("账号未注册")
        if login_flag:
            return True
        else:
            return False

    def login_pwd_error(self):
        self.login_handle.send_user("18600407736")
        self.login_handle.send_pwd("orange1")
        self.login_handle.click_login()
        login_flag = self.login_handle.get_tost_result("登录密码错误")
        if login_flag:
            return True
        else:
            return False

if __name__ == '__main__':
    login = LoginBusiness(0)
    login.login_user_error()


