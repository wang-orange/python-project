#coding:utf-8
from appium import webdriver

class PulseTakingDriver:
	def driver(self):
		caps = {
		'platform': 'Android',
		'app': 'E:\\03-脉诊项目\\apk\\'
		}