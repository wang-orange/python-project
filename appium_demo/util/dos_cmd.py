#coding=utf-8
import os

class DosCmd:
    '''
    执行dos命令
    '''
    def execute_cmd_result(self, command):
        result_list = []
        fr = os.popen(command)
        result = fr.readlines() ##
        # print result
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip())  # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        return result_list

    def execute_cmd(self, command):
        os.system(command)

if __name__ == '__main__':
    dos = DosCmd()
    print dos.execute_cmd_result('adb devices')
    # print dos.execute_cmd_result("netstat -ano|findstr 8888")
    # command = 'move E:\\download-facetongue\\*.jpg E:\\temp-test\\1a7729ee7bfc4c0e8faf73f7abee24a2.jpg'
    # print command
    # os.system(command)
    print dos.execute_cmd_result('adb shell ls -l /mnt/internal_sd/TongueStorage/Photo/')



