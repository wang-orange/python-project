# coding:utf-8

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://bj.ganji.com")
driver.implicitly_wait(10)
# 获取当前窗口句柄
h = driver.current_window_handle
print h
# 打开新的窗口
driver.find_element_by_css_selector(".dt-t").click()
# 获取所有句柄
all_h = driver.window_handles
print all_h
# 切换句柄：获取list里面第二个直接切换
driver.switch_to.window(all_h[1])
print driver.title  #打印页面title
# 关闭新窗口，切回主页
driver.close()
# 切换到首页句柄
driver.switch_to.window(h)
# 打印当前title
print driver.title