import numpy as np
from math import sqrt
from collections import Counter
from .metrics import accuracy_score

class KNN_Classify():
	def __init__(self, k):
		""" 初始化KNN分类器 
		"""
		assert k >= 1, "k must be valid"
		self.k = k
		self._X_train = None
		self._y_train = None
	
	def fit(self, X_train, y_train):
		""" 根据训练数据集X_train和y_train训练KNN分类器 
		"""
		assert X_train.shape[0] == y_train.shape[0], \
		"The size of X_train must be equal to the size of y_train"
		assert self.k <= X_train.shape[0], \
		"The size of X_train must be at least k."
		
		self._X_train = X_train
		self._y_train = y_train
		return self
	
	def predict(self, X_predict):
		""" 给定待预测数据集X_predict,返回表示X_predict的结果向量 
		"""
		assert X_predict.ndim >= 2, ("X_predict expected 2D array, got 1D array instead: array=%s.\n" %X_predict + \
		"Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample")
		assert self._X_train is not None and self._y_train is not None, \
		"must fit before predict !"
		assert X_predict.shape[1] == self._X_train.shape[1], \
		"the feature of X_predict must be equal to X_train"
		
		y_predict = np.array([self._predict(x) for x in X_predict])
		return y_predict
	
	def _predict(self, x):
		""" 给定单个待预测数据x(向量)，返回x的预测结果 
		"""
		assert x.shape[0] == self._X_train.shape[1], \
		"the feature of x must be equal to  X_train"
		
		# 样例x与训练集中各元素的距离（欧拉距离）
		distances = [sqrt(np.sum((x_train - x)**2)) for x_train in self._X_train] 
	
		# 距离由小到大排列后元素对应的索引
		nearest = np.argsort(distances)
	
		# 前k个索引所属的类别
		topK_y = [self._y_train[i] for i in nearest[:self.k]]
	
		# 汇总类别出现的次数
		votes = Counter(topK_y)
	
		# 找出得票最多的那个
		return votes.most_common(1)[0][0]
	
	def score(self, X_test, y_test):
		''' 根据测试数据集 X_test 和 y_test 确定当前模型的准确度
		'''
		y_predict = self.predict(X_test)
		return accuracy_score(y_test, y_predict)

	def __repr__(self):
		return "KNN(k=%d)" %self.k
	
	
	
	
	
	
	
	
	
	
	
	
		
