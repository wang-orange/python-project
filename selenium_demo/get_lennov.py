# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"博客")
# 获取百度输入框中的联想词
bk = driver.find_elements_by_class_name("bdsug-overflow")
print bk
for i in bk:
    print i.get_attribute("data-key")
time.sleep(2)
# 点击其中的一个，如第二个联想词
if len(bk)>1:
    bk[1].click()
else:
    print "未获取到匹配的词"