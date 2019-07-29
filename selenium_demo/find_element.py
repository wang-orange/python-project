# coding:utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.baidu.com")
# time.sleep(3)
# 1.通过id定位百度搜索框，并输入“python”
#browser.find_element_by_id("kw").send_keys("python")
# 2.通过name定位百度搜索框，并输入“python”
#browser.find_element_by_name("wd").send_keys("python")
# 3.通过class定位百度搜索框，并输入“python”
#browser.find_element_by_class_name("s_ipt").send_keys("python")
# 4.通过tag（标签）定位百度搜索框，并输入“python”,应该会报错，因为一个页面中相同的标签有很多
#browser.find_element_by_tag_name("input").send_keys("python")
# 5.定位页面上的超链接,并点击
#browser.find_element_by_link_text("hao123").click()
# 6.通过partial_link 模糊匹配
#browser.find_element_by_partial_link_text("o123").click()
# 7.在FirePath里copy出xpath地址
#browser.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
# 8.通过css定位
browser.find_element_by_css_selector("#kw").send_keys("python")
browser.find_element_by_id("su").click()

