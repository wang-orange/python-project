# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
url = "http://www.baidu.com"
driver.implicitly_wait(10)
driver.get(url)
''' 1.鼠标移动到“设置” '''
mouse = driver.find_element_by_link_text("设置")  # 定位“设置”所在的位置
ActionChains(driver).move_to_element(mouse).perform()  # 将鼠标移动到“设置”上
driver.find_element_by_css_selector(".setpref").click()  # 点击“搜索设置”
''' 2.定位到select选项 '''
# s = driver.find_element_by_id("nr")  # 定位select下拉框
# s.find_element_by_xpath("//option[2]").click()  # 点击下拉框中的第二个选项
# driver.find_element_by_id("nr").find_element_by_xpath("//option[2]").click()  # 合并成一步
# driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()  # 直接通过xpath定位
# driver.find_element_by_css_selector("select#nr>option:nth-child(2)").click()  # 直接通过css定位
''' 3.通过Select定位 '''
s = driver.find_element_by_id("nr")
Select(s).select_by_index(2)  # 通过索引（从0开始）定位
# Select(s).select_by_value("20")  # 通过value定位
# Select(s).select_by_visible_text("每页显示50条") # 通过text定位
# Select(s).deselect_by_index(2)  # NotImplementedError: You may only deselect options of a multi-select
