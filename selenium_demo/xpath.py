# coding:utf-8
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
''' 1.xpath通过属性定位 '''
#browser.find_element_by_xpath(".//*[@id='kw']").send_keys("python") #通过id属性定位
#browser.find_element_by_xpath(".//*[@name='wd']").send_keys("python") #通过name属性定位
#browser.find_element_by_xpath(".//*[@class='s_ipt']").send_keys("python") #通过class属性定位
#browser.find_element_by_xpath(".//*[@autocomplete='off']").send_keys("python") #通过其他属性定位(用*表示任意标签)
#browser.find_element_by_xpath(".//input [@autocomplete='off']").send_keys("python") #用具体标签
''' 2.xpath层级定位 '''
#browser.find_element_by_xpath("//span[@class='bj s_ipt_wr']/input").send_keys("python") #通过老爸定位
#browser.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python") #通过爷爷定位
''' 3.xpath通过索引定位（兄弟元素跟它的标签一样时） '''
#browser.find_element_by_xpath("//div[@id='u1']/a[1]").click() #定位老大
#browser.find_element_by_xpath("//div[@id='u1']/a[2]").click() #定位老二
#browser.find_element_by_xpath("//div[@id='u1']/a[3]").click() #定位大三
''' 4.xpath逻辑运算（and or not）'''
#browser.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").send_keys("python")
''' 5.xpath模糊匹配功能 '''
# browser.find_element_by_xpath("//*[contains(text(),'o123')]").click()
# browser.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys("python") #模糊匹配某一个属性
# browser.find_element_by_xpath("//*[starts-with(@class,'s_i')]").send_keys("python") #模糊匹配以什么开头
# browser.find_element_by_xpath("//*[ends-with(@id,'kw')]") #模糊匹配以什么结尾（报错SyntaxError: The expression is not a legal expression.）
# browser.find_element_by_xpath("//*[matchs(text(),'hao123')]").click() #最强匹配（报错SyntaxError: The expression is not a legal expression.）

