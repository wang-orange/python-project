# coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
mouse = driver.find_element_by_link_text("更多产品")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
# p = driver.find_element_by_name("tj_more")
# # 经确认，是可以定位到元素的
# print p.text
# # 这一步点击失效了
# p.click()
# js大法，完美解决click失效问题
js = 'document.getElementsByName("tj_more")[0].click()'
driver.execute_script(js)