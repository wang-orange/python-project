# coding:utf-8
from selenium import webdriver

'''
**********************************************************************************************
以后在firebug中查看元素的Xpth时，一定要记得看右上角，只要元素对应的导航条有iframe的字样，
就必须切换对应的iframe才能定位到元素；
记得：当iframe上的操作完后，想重新回到主页面上操作元素，例如：登录成功后进入邮箱详情界面的时候，
就可以用switch_to.default_content()方法返回到主页面，否则用户的操作总在iframe范围内，还是无法定位到元素。
***********************************************************************************************
browser.find_element_by_class_name("j-inputtext dlemail").send_keys(name)
直接复制过来用class属性(j-inputtext dlemail)定位是会报错的:
InvalidSelectorError: Compound class names not permitted
class属性有空格表示被赋予了多个类，定位的时候取其中的一个就行（并且要唯一），也就是说class="j-inputtext dlemail"，
取j-inputtext 和dlemail都是可以的，这样这个class属性在页面上唯一就行；
判断元素唯一性:
F12切换到HTML界面，在搜索框输入关键字搜索，如：j-inputtext，然后按回车搜索，
看页面上有几个class属性中有j-inputtext这个属性的，就知道是不是唯一的了.
********************************************************************************************
def byId(name,pwd):
    browser.find_element_by_id('auto-id-1535338460987').send_keys(name)
    browser.find_element_by_id('auto-id-1535338460988').send_keys(pwd)
会报错，因为此时id是动态变化的，新打开后，会变化。
********************************************************************************************
'''
browser = webdriver.Firefox()
browser.get("http://mail.163.com")
browser.implicitly_wait(30)

# 切换iframe
# browser.switch_to.frame("x-URS-iframe") #通过iframe的id切换
# 如果iframe没有id属性和name属性为空时，需要先定位iframe元素
# iframe = browser.find_element_by_tag_name("iframe") # 先通过tag定位
iframe = browser.find_element_by_id("x-URS-iframe") # 通过id定位
browser.switch_to.frame(iframe) # 切到对应的iframe

# 通过name定位
def byName(name,pwd):
    browser.find_element_by_name("email").send_keys(name)
    browser.find_element_by_name("password").send_keys(pwd)
# 通过class定位
def byClassName(name,pwd):
    browser.find_element_by_class_name("dlemail").send_keys(name)
    browser.find_element_by_class_name("dlpwd").send_keys(pwd)

if __name__ == '__main__':
    byName("123","456")
    # byClassName("aaa","bbb")
    # 释放iframe，回到主界面
    browser.switch_to.default_content()


