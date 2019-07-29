#coding=utf-8
import unittest
# Python27\Lib目录下如果没有HTMLTestRunner.py,需从http://tungwaiyip.info/software/HTMLTestRunner.html 中将其拷贝到该目录下
import HTMLTestRunner
import os
import threading
import multiprocessing
from appium import webdriver
from business.login_business import LoginBusiness
import time
from util.server import Server

class ParaTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParaTestCase,self).__init__(methodName)
        global para
        para = parame

class MyTestCase(ParaTestCase):
    @classmethod
    def setUpClass(cls):
        print "This is setUpClass"
        print "setUpClass-->" , para
        cls.login_business = LoginBusiness(para)

    @classmethod
    def tearDownClass(cls):
        print "This is tearDownClass"

    # def setUp(self):
    #     print "This is setUP"
    #
    # def tearDown(self):
    #     print "This is tearDown"

    def test_01(self):
        print "This is test_01"
        print "test_01里面的参数", para
        u' 测试账号未注册 '
        flag = self.login_business.login_user_error()
        # try:
        #     self.assertTrue(flag)
        # except:
        #     print "提示错误"


    # @unittest.skip("CaseTest")
    def test_02(self):
        print "This is test_02"
        print "test_02里面的参数", para
        u' 测试登录密码错误 '
        flag = self.login_business.login_pwd_error()
        # try:
        #     self.assertTrue(flag)
        # except:
        #     print "提示错误"

    def test_03(self):
        print "This is test_03"
        print "test_03里面的参数", para
        u' 登录成功 '
        self.login_business.login_success()

def appium_init():
    server = Server()
    server.main()
    return server.device_list

def get_suite(i):
    suite = unittest.TestSuite()
    print "get_suit里面的", i
    suite.addTest(MyTestCase(methodName='test_01', parame=i))
    suite.addTest(MyTestCase("test_02", parame=i))
    suite.addTest(MyTestCase('test_03',parame=i))
    # unittest.TextTestRunner().run(suite)
    # report_file = os.path.join(os.path.dirname(os.path.realpath('')), 'report', 'report'+str(i)+'.html')  # 绝对路径
    report_file = '../report/report_'+str(i)+'.html'  # 相对路径
    fp = file(report_file, 'wb')
    HTMLTestRunner.HTMLTestRunner(fp, title=u'imooc自动化测试', description=u'登录页面测试').run(suite)

if __name__ == "__main__":
    device =  appium_init()
    time.sleep(20)
    threads = []
    for i in range(len(device)):
        # thread = threading.Thread(target=get_suite, args=(i,))  # 多线程时可能存在问题，可改用多进程
        thread = multiprocessing.Process(target=get_suite, args=(i,))
        thread.start()



