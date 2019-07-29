#coding:utf-8
from util.dos_cmd import DosCmd
import time
from util.server import Server
from base.mirror_driver import MirrorDriver
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class CheckFaceTongue:
	'''
	1 将待验证图片下载到“E:\\FaceTongueDownload”目录下（人工操作，其他步骤程序自动进行）
    2 镜子端拍照
    3 获取拍照图片名称
    4 将1中的图片更名后移动到“E:\\temp-test”下
    5 将4中的图片push到镜子的“/mnt/internal_sd/TongueStorage/Photo/”目录下
    6 点击分析按钮
    7 查看结果
	'''
	def __init__(self):
		self.dos = DosCmd()
		# self.file_name = self.get_file_name()

	def get_file_name(self):
		'''
		找到最新拍照的图片名称
		'''
		command = 'adb shell ls -l /mnt/internal_sd/TongueStorage/Photo/'
		jpg = self.dos.execute_cmd_result(command)
		print jpg
		date = []
		for temp in jpg:
			sub = temp.split()
			time = sub[4]+' '+sub[5]
			date.append(time)
		print date
		index = self.max_list(date)
		if index !=None:
			latest_file = jpg[index].split()[6]
			return latest_file
		else:
			return None

	def max_list(self,li):
		'''
		定位列表中的最大值，并返回其下标
		'''
		if len(li)>0:
			max = li[0]
			index = 0
			for i in range(len(li)):
				if max < li[i]:
					max = li[i] 
					index = i
			return index
		else:
			return None
		
	def move_modify(self,file_name):
		'''
		将图片拷贝到待测目录下
		'''
		src_path = "E:\\FaceTongueDownload\\"
		dest_path = "E:\\temp-test\\"
		if file_name != None:
			command = 'move '+ src_path +'*.jpg '+ dest_path + file_name
			print 'command:',command
			self.dos.execute_cmd(command)

	def push_file(self,file_name):
		'''
		将图片push到镜子端的‘/mnt/internal_sd/TongueStorage/Photo/’目录下
		'''
		if file_name !=None:
			# 先删除镜子端的图片
			rm_code = 'adb shell rm /mnt/internal_sd/TongueStorage/Photo/*'
			self.dos.execute_cmd(rm_code)
			command = "adb push E:\\temp-test\\"+file_name+" /mnt/internal_sd/TongueStorage/Photo/"
			print command
			self.dos.execute_cmd(command)

	def is_jpg(self):
		''' 判断“E:\\FaceTongueDownload” 下是否存在jpg文件
		'''
		command = "dir /B E:\\FaceTongueDownload\\*.jpg"
		re = self.dos.execute_cmd_result(command)
		if re == []:
			return False
		else:
			return True

	def run_main(self):
		file_name = self.get_file_name()
		print 'file_name:', file_name
		self.move_modify(file_name)
		time.sleep(3)
		self.push_file(file_name)

def server_init():
	server = Server()
	server.main()

if __name__ == '__main__':
	# 1-启动appium服务
	server_init()
	time.sleep(15)
	test_flag = ['face', 'tongue']
	mirror = MirrorDriver(0)
	face = CheckFaceTongue()
	mirror.main_interface()
	
	while 1:
		# 有待处理的图片时
		if face.is_jpg():
		    # 2-拍照
		    mirror.go_take_photos(test_flag[1]) # 0-面部检测； 1-舌部检测；需手动修改
		    time.sleep(4)
		    # 3-替换图片
		    face.run_main() 
		    # 4-分析图像
		    mirror.analyze_photo()
		else:
			print "请放入图片......"
			time.sleep(10)
			mirror.driver.tap([(630,303),(760,350)], 100) # 点击屏幕，防止超时无操作断开会话
    	
		
    

	



