#coding=utf-8
from ConfigParser import ConfigParser

class ReadIni:
    '''
    从配置文件ini中读取元素的信息
    '''
    def __init__(self, ini_path=None):  # 构造器
        if ini_path == None:
            self.file_path = "../config/LoginElement.ini"  # 默认路径
        else:
            self.file_path = ini_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = ConfigParser()
        read_ini.read(self.file_path)
        # print read_ini
        return read_ini

    def get_value(self, key, section=None):  # 默认参数(section)应放在最后的位置
        '''
        通过key获取对应的value
        '''
        if section == None:
            section = 'login_element'
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value

if __name__ == "__main__":
    read_ini = ReadIni()
    print read_ini.get_value("username")
    print read_ini.get_value("password")
    print read_ini.get_value('course', 'course_element')
    print read_ini.get_value('cour', 'course_element')
    print read_ini.get_value('course', 'course_el')






