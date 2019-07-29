#coding=utf-8
from read_ini import ReadIni

class GetByLocation:
    '''
    从配置文件中读取元素的信息，然后进行定位
    '''
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        value = read_ini.get_value(key)
        if value !=None:
            by = value.split('>')[0]
            by_value = value.split('>')[1]
            print by, by_value
            if by == 'id':
                return self.driver.find_element_by_id(by_value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(by_value)
            else:
                return self.driver.find_element_by_xpath(by_value)
        else:
            return None























