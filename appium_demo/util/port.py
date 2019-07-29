#coding=utf-8
from dos_cmd import DosCmd

class Port:
    def port_is_used(self, port_number):
        '''
        判断端口是否被占用
        '''
        flag = None
        dos = DosCmd()
        result = dos.execute_cmd_result("netstat -ano|findstr "+str(port_number))
        # print result
        if len(result)>0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, devices_list):
        '''
        根据devices个数生成对应个数的可用端口
        '''
        port_list = []
        if devices_list != None:
            while len(port_list) != len(devices_list):  # 生成跟devices相同数量的端口
                if self.port_is_used(start_port) == False:  # 端口start_port未被占用，就添加进port_list
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print "生成可用端口失败"
            return None


if __name__ == '__main__':
    port = Port()
    li = [1,2,3,4]
    # print port.port_is_used(1234)
    print port.port_is_used(4720)
    print port.create_port_list(8888, li)
    print port.create_port_list(4719,None)



