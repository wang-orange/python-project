#coding=utf-8
from dos_cmd import DosCmd
from port import Port
import threading
from write_user_command import WriteUserCommand
import time

# split(str="", num=string.count(str))
# 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数

class Server:
    ''' 
    根据设备信息启动对应的appium服务
    '''
    def __init__(self):
        self.dos = DosCmd()
        self.wr = WriteUserCommand()
        self.device_list = self.get_devices()

    def get_devices(self):
        '''
        获取devices信息
        '''
        devices_list = []
        result = self.dos.execute_cmd_result("adb devices")
        # print result
        if len(result) >= 2:
            for i in result:
                if 'List' in i:
                    continue
                if 'device' in i:
                    list = i.split('\t')
                    # print 'list:', list
                    devices_list.append(list[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        '''
        获取可用端口信息
        '''
        port = Port()
        port_list = port.create_port_list(start_port, self.get_devices())
        return port_list

    def create_command_list(self, i):
        '''
        组装启动appium的命令列表
        '''
        # appium -p 4700 -bp 4721 -U deviceName
        command_list = []
        port_list = self.create_port_list(4700)
        bp_port_list = self.create_port_list(4900)
        command = 'appium -p '+ str(port_list[i]) + ' -bp ' + str(bp_port_list[i]) + ' -U ' + self.device_list[i] +' --no-reset --session-override '
        command_list.append(command)
        self.wr.write_file(i, port_list[i], bp_port_list[i], self.device_list[i])
        return command_list

    def start_server(self, i):
        '''
        启动appium
        '''
        start_list = self.create_command_list(i)
        print start_list
        self.dos.execute_cmd(start_list[0])

    def kill_server(self):
        '''
        回
            收appium相关进程
        '''
        server_list = self.dos.execute_cmd_result('tasklist | findstr node.exe')
        if len(server_list)>0:
            self.dos.execute_cmd('taskkill /F /PID node.exe')


    def main(self):
        '''
        利用多线程启动多个appium服务
        '''
        self.kill_server()  # 先回收已启动的进程
        self.wr.clear_data()  # 清空yaml文件
        if self.device_list:
            for i in range(len(self.device_list)):  # 有多少个设备，就启动多少个线程
                appium_start = threading.Thread(target=self.start_server, args=(i,))
                appium_start.start()
        # time.sleep(15)

if __name__ == '__main__':
    server = Server()
    # print server.get_devices()
    # print server.create_command_list()
    server.main()


