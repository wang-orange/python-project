# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/wangyjketang/")

# 1.通过id定位
js = 'document.getElementById("blog_nav_admin").click()'
driver.execute_script(js)
# 2.通过class定位
time.sleep(2)
js = 'document.getElementsByClassName("input-text")[0].value="汪orange";'  # 输入账号
driver.execute_script(js)
js2 = 'document.getElementsByClassName("input-text")[1].value="orange0419";'  # 输入密码
driver.execute_script(js2)
# 3.通过css定位
time.sleep(2)
js = 'document.querySelectorAll("#signin")[0].click()'  # 点击登录按钮
driver.execute_script(js)