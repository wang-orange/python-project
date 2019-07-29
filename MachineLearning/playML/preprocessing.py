import numpy as np 


class StandardScaler():
          def __init__(self):
                    self.mean_ = None
                    self.scale_ = None
          
          def fit(self, X):
                    ''' 根据训练数据集获得数据的均值和方差
                    '''
                    assert X.ndim == 2, "The dimension of X must be 2"

                    self.mean_ = np.array(np.mean(X[:, i]) for i in range(X.shape[1]))
                    self.scale_ = np.array(np.std(X[:, i]) for i in range(X.shape[1]))
                    return self
          
          def transform(self, X):
                    ''' 将X根据StandardScaler进行均值方差归一化处理
                    '''
                    assert X.ndim == 2, "The dimension of X must be 2"
                    assert self.mean_ != None and self.scale_ != None, \
                              "must fit before transform"
                    assert X.shape[1] == self.mean_.shape[0], \
                              "the feature of X must be equal to mean_ and scale_"
                    
                    resX = np.array(size=X.shape, dtype=float)
                    for col in range(X.shape[1]):
                              resX[:, col] = np.array((X[:, col] - self.mean_[col]) / self.scale_[col] 
                    
                    return resX