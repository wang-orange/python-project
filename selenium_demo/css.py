# coding:utf-8
from selenium import webdriver
"""
css用#号表示id属性，如#kw
css用.表示class属性，如.s_ipt
css直接用标签名称，无任何标识符，如input
"""
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
''' 1.css通过属性定位 '''
#driver.find_element_by_css_selector("#kw").send_keys("python") #通过id属性定位
#driver.find_element_by_css_selector("[id='kw']").send_keys("python")
#driver.find_element_by_css_selector(".s_ipt").send_keys("python") #通过class属性定位
#driver.find_element_by_css_selector("[class='s_ipt']").send_keys("python")
#driver.find_element_by_css_selector("[name='wd']").send_keys("python") #通过name属性定位
#driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python") #通过autocomplete定位
#driver.find_element_by_css_selector("[type='hidden']") #通过type属性定位
''' 2.css通过标签和属性的组合定位 '''
#driver.find_element_by_css_selector("input:contains('wd')") #InvalidSelectorError: An invalid or illegal selector was specified
#driver.find_element_by_css_selector("input#kw").send_keys("python") #通过标签与id属性定位
#driver.find_element_by_css_selector("input[id='kw']").send_keys("python")
#driver.find_element_by_css_selector("input.s_ipt").send_keys("python") #通过标签与class属性定位
#driver.find_element_by_css_selector("input[class='s_ipt']").send_keys("python")
#driver.find_element_by_css_selector("input[autocomplete='off']").send_keys("python") #通过标签与其他属性组合定位
''' 3.css通过层级关系定位 '''
#driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python")
#driver.find_element_by_css_selector("form#form>span>input").send_keys("python") #通过id
#driver.find_element_by_css_selector("form[id='form']>span>input").send_keys("python")
#driver.find_element_by_css_selector("form.fm>span>input").send_keys("python") #通过class
''' 4.css通过索引定位 '''
#driver.find_element_by_css_selector("div#u1>a:nth-child(1)").click() #第一孩子
#driver.find_element_by_css_selector("div#u1>a:nth-child(7)").click() #第七孩子
''' 5.css逻辑运算，与xpath不同，无需写and关键字 '''
#driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")


