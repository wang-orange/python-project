# coding:utf-8
# 导入time模块
import time
# 第一步：导入webdriver模块
from selenium import webdriver
# 第二步：打开浏览器
driver = webdriver.Firefox()
# 第三步：打开百度
driver.get("http://www.baidu.com")
# 通过js来新开一个窗口
js = 'window.open("http://www.sogou.com");'
driver.execute_script(js)
# 设置休眠时间3秒，也可以是小数
time.sleep(3)
driver.get("http://www.hordehome.com")
time.sleep(5)
# 等待3秒后刷新页面,相当于浏览器输入框后面的刷新按钮
driver.refresh()
# 返回上一页，相当于浏览器左上角的左箭头按钮
driver.back()
time.sleep(3)
# 切换到一下页，相当于浏览器左上角的右键头按钮
driver.forward()
# 设置窗口大小为540*960
driver.set_window_size(540,960)
time.sleep(2)
# 将浏览器窗口最大化
driver.maximize_window()
# 截屏后指定保存路径+文件名称+后缀
driver.get_screenshot_as_file("f:\\test.jpg")
#driver.close()  #关闭当前窗口
driver.quit()  #退出浏览器进程