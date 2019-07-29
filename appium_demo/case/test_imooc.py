# coding:utf-8
from appium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.read_init import ReadIni
from util.get_by_location import GetByLocation

def get_driver():
    desired_caps = {
        'platformName':'Android',
        # 'automationName':'UiAutomator2',  # 测试平台，默认Appium，但定位tost元素必须用UiAutomator2，并且android版本必须5以上
        'deviceName':'8c76cc8f',
        'app':'F:\\AutoTest\\工具\\mukewang.apk',
        # 'app':'F:\\AutoTest\\工具\\baiduyuedu_5891.apk',
        # 'appWaitActivity':'com.imooc.component.imoocmain.index.MCMainActivity',
        'noReset':True  # 不用每次都重新安装apk
        }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # driver.implicitly_wait(30)
    return driver

def get_size():
    size = driver.get_window_size()
    print size
    return size

def swipe_left():
    size = get_size()
    width = size['width']
    height = size['height']
    x1 = width/10*9
    x2 = width/10
    y = height/2
    driver.swipe(x1,y,x2,y)

def swipe_right():
    size = get_size()
    width = size['width']
    height = size['height']
    x1 = width/10*9
    x2 = width/10
    y = height/2
    driver.swipe(x2,y,x1,y)

def swipe_up():
    size = get_size()
    width = size['width']
    height = size['height']
    x = width/2
    y1 = height/10*9
    y2 = height/10
    driver.swipe(x,y1,x,y2)

def swipe_down():
    size = get_size()
    width = size['width']
    height = size['height']
    x = width/2
    y1 = height/10*9
    y2 = height/10
    driver.swipe(x,y2,x,y1)

def swipe_on(direction):
    if direction == 'left':
        swipe_left()
    elif direction == 'right':
        swipe_right()
    elif direction == 'up':
        swipe_up()
    else:
        swipe_down()

def go_login():
    element = driver.find_element('id', 'cn.com.open.mooc:id/tab_layout')  # 层级定位
    elements = element.find_elements_by_class_name("android.widget.RelativeLayout")
    elements[3].click()  # 点击“我的”
    print "进入注册界面"
    time.sleep(2)
    driver.find_element_by_id("cn.com.open.mooc:id/rl_login_before").click()
    print "进入登录界面"
    time.sleep(2)
    driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login").click()
    # 通过class定位
    # elements = driver.find_elements_by_class_name("android.widget.TextView")
    # print len(elements)
    # elements[5].click()

def login():  # 通过id定位
    time.sleep(2)
    get_by_location = GetByLocation(driver)
    get_by_location.get_element('username').send_keys("11111111111111")
    get_by_location.get_element('password').send_keys("22222222")
    get_by_location.get_element('login_button').click()

def login_by_node():  # 层级定位
    element = driver.find_element_by_id("android:id/content")
    elements = element.find_elements_by_class_name("android.widget.EditText")
    elements[0].send_keys("12345678")
    elements[1].send_keys("1234")
    driver.find_element('id', 'cn.com.open.mooc:id/login').click()

def login_by_uiautomator():
    driver.find_element_by_android_uiautomator('new UiSelector().text("12345678")').clear()
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys("18877771234")
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').send_keys('3333335')
    driver.find_element('id', 'cn.com.open.mooc:id/login').click()

def login_by_xpath():
    # driver.find_element_by_xpath('//*[contains(@text,"忘记")]').click()  # 点击“忘记密码”
    # driver.find_element_by_xpath('//android.widget.TextView[@text="忘记密码"]').click()
    # 定位叔节点的子节点（关键字preceding-sibling::）
    driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::android.widget.LinearLayout').send_keys('111111')  # 通过class定位
    driver.find_element_by_xpath('//android.widget.TextView[@resource-id="cn.com.open.mooc:id/login_lable"]/../preceding-sibling::*[@index="4"]').send_keys("2222222")  # 通过index定位

def get_web_view():
    time.sleep(3)  
    driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text("猿问")').click()
    time.sleep(3)
    driver.find_elements_by_xpath('//*[@resource-id="cn.com.open.mooc:id/tv_title"]')[2].click()
    webview = driver.contexts  # 获取上下文，类似selenium中的handle
    print webview
    for view in webview:
        if 'WEBVIEW_cn.com.open.mooc' in view:
            driver.switch_to.context(view)
            break
    driver.find_element_by_link_text("关注").click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
    driver.switch_to.content(webview[0])  # 切回

def get_tost():
    time.sleep(3)
    driver.find_element_by_id("cn.com.open.mooc:id/account_edit").send_keys("232323232")
    tost_element = ('xpath', '//*[contains(@text,"请输入密码")]')
    while True:
        driver.find_element('id', 'cn.com.open.mooc:id/login').click()
        try:
            print WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))
        except:
            print "No find element!"
        else:
            break


if __name__ == "__main__":
    driver = get_driver()
    time.sleep(5)
    # swipe_on('left')
    # time.sleep(1)
    # swipe_on('left')
    # time.sleep(1)
    # swipe_on('left')
    # time.sleep(1)
    # swipe_on('up')
    # time.sleep(3)
    # w = get_size()['width']/2
    # h = get_size()['height']/2
    # driver.tap([(w,h),(w,h)])  # 点击弹出的新人红包框
    go_login()
    login()
    # login_by_node()
    # login_by_uiautomator()
    # login_by_xpath()
    # get_web_view()
    # get_tost()


