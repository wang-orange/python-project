import numpy as np 
from sklearn import datasets


def train_test_split(X, y, test_ratio=0.2, seed=None):
          """ 将数据X、y按照 test_ratio 分割成X_train、y_train、X_test、y_test 
          """
          assert X.shape[0] == y.shape[0], \
                    "the size of X must be equal to y"
          assert 0.0 <= test_ratio <= 1.0, \
                    "test_ratio must be valid"
          
          if seed:
                    np.random.seed(seed)
          
          shuffle_indexes = np.random.permutation(len(X))  # 打乱顺序的索引列表
          test_len = int(len(X) * test_ratio)
          test_indexes = shuffle_indexes[:test_len]  # 测试集索引列表
          train_indexes = shuffle_indexes[test_len:]  # 训练集索引列表
          X_test = X[test_indexes]  # 测试集
          y_test = y[test_indexes]  # 测试集对应的标签
          X_train = X[train_indexes]  # 训练集
          y_train = y[train_indexes]  # 训练集对应的标签
          return X_train, X_test, y_train, y_test


