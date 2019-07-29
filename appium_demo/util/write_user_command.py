#coding=utf-8
import yaml  # 安装yaml：pip install pyyaml

class WriteUserCommand:
	def read_file(self):
		'''
		读取yaml文件
		'''
		with open("..\\config\\UserConfig.yaml") as fp:
		   data = yaml.load(fp)  # yaml文件中冒号后必须有空格？
		return data

	def get_value(self, user, key):
		'''
		获取value
		'''
		data = self.read_file()
		if data:
			value = data[user][key]
			return value

	def write_file(self, i, port, bp, deviceName):
		'''
		写入数据
		'''
		data = self.join_data(i, port, bp, deviceName)
		# print data
		with open("..\\config\\UserConfig.yaml",'a') as fr:
			yaml.dump(data, fr)

	def clear_data(self):
		'''
		清空yaml文件
		'''
		with open("..\\config\\UserConfig.yaml", 'w') as fr:
			fr.truncate()

	def join_data(self, i, port, bp, deviceName):
		'''
		拼接数据
		'''
		# user_info_0: {port: 4700, bp: 4900, deviceName: '8c76cc8f'}
		data = {
		'user_info_'+str(i):{'port':port,'bp':bp,'deviceName':deviceName}
		}
		return data

if __name__ == '__main__':
	write_file = WriteUserCommand()
	print write_file.read_file()
	print write_file.get_value('user_info_1', 'bp')
	write_file.write_file(5, 1234, 4567, 'jjj111')
	# write_file.clear_file()



