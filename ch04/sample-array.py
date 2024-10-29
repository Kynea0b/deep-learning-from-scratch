
import numpy as np
import matplotlib.pylab as plt

# https://note.nkmk.me/python-numpy-ndarray-sum-mean-axis/
# https://note.nkmk.me/python-numpy-arange-linspace/

print(np.arange(3))
# [0 1 2]

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(np.sum(a**2))
# 66


#* numpify *#
# numpy配列として生成するとブロードキャスト機能になる
def function_2(x):
	return np.sum(x**2)

# b ≠ [1, 2, 3] はlistはサポートしないのエラーとなる。
a = np.array([1, 2, 3])
res = function_2(a)
print("二乗和", res)

print("---")
for key in ('W1','B1','W2','B2'):
    print("hoge")
    print(key)

# params = {"W1":1, "B1":2, "W2":2, "B2":2}

