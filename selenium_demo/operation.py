# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''
1.点击（鼠标左键）页面按钮：click()
2.清空输入框：clear()
3.输入字符串：send_keys(),如果发中文，前面需加u，如u"中文"
4.submit提交表单，一般模拟回车键
5.键盘操作：
  模拟键盘操作需要先导入键盘模块：from selenium.webdriver.common.keys import Keys
  1)模拟enter键:send_keys(Keys.ENTER)
  2)键盘F1-F12:send_keys(Keys.F1) 把F1换成对应的快捷键
  3)复制Ctrl+C:send_keys(Keys.CONTROL,'c')
  4)粘贴Ctrl+V:send_keys(Keys.CONTROL,'v')
  5)全选Ctrl+A:send_keys(Keys.CONTROL,'a')
  6)剪切Ctrl+X:send_keys(Keys.CONTROL,'x')
  7)制表键Tab:send_keys(Keys.TAB)
6.鼠标悬停事件
  鼠标事件需要先导入模块：from selenium.webdriver.common.action_chains import ActionChains
  1)perform()执行所有ActionChains
  2)move_to_element()鼠标悬停
  3)context_click()右键鼠标
  4)double_click()双击鼠标
'''
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# implicitly_wait 是隐式等待，作用全局
driver.implicitly_wait(10)
# driver.find_element_by_css_selector("#kw").send_keys(u"软件测试")
# driver.find_element_by_id("su").click()
# time.sleep(3)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
# driver.find_element_by_id("kw").submit()
# time.sleep(3)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys(u"测试")
# driver.find_element_by_id("kw").send_keys(Keys.ENTER)
mouse = driver.find_element_by_link_text("设置")
#child = driver.find_element_by_css_selector("div.bdpfmenu>a.setpref")
action = ActionChains(driver) #定义ActionChains
action.move_to_element(mouse).perform()




