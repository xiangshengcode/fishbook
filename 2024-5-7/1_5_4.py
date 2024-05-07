import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[4,4],[3,7]])

print(A*B)
##广播扩展形状不同的数组

B = B.flatten()
##转换为一维数组 

print(B[np.array([0,2,3])])
##获取索引