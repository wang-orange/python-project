# coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//div[@id='u1']/a[.='登录']").click()
#driver.find_element_by_css_selector("#TANGRAM__PSP_10__footerULoginBtn").click()
#driver.find_element_by_xpath("//p[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
#driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName").click()

