# coding:utf-8
import random
from selenium import webdriver
'''
print random.random()    # 产生 0 到 1 之间的随机浮点数
print random.randint(0,9)  # 产生 1 到 10 的一个整数型随机数
print random.uniform(1,9.8)  # 产生  1到 9.8 之间的随机浮点数，区间可以不是整数
print random.choice('tomorrow')  # 从序列中随机选取一个元素
print random.randrange(1,100,2)  # 生成从1到100的间隔为2的随机整数
'''
'''
implicitly_wait():隐式等待
当使用了隐士等待执行测试的时候，如果WebDriver没有在DOM中找到元素，将继续等待，
超出设定时间后则抛出找不到元素的异常，换句话说，当查找元素或元素并没有立即出现的时候，
隐式等待将等待一段时间再查找DOM，默认的时间是0
一旦设置了隐式等待，则它存在整个WebDriver对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
'''
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.implicitly_wait(10) # 隐式等待10秒
browser.find_element_by_id("kw").send_keys(u"测试部落")
browser.find_element_by_id("kw").submit()
s = browser.find_elements_by_css_selector("h3.t>a")
print s
# for i in s:
#      print i.get_attribute("href")
t = random.randint(0,9) # 设置随机数
a = s[t].get_attribute("href") # 随机取一个结果获取url地址
browser.get(a)
# s[t].click()
