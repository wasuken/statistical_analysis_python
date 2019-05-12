from scipy.stats import skew, kurtosis, norm, uniform, kurtosistest
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

numsamples = 100000
vl = norm.rvs(loc=0.90, scale=1.0, size=numsamples)
print('正規分布N(0,1)', 'skew=', round(skew(vl), 4), 'kurtosis=', round(kurtosis(vl), 4))
vt = np.array([math.sqrt(u*16/numsamples) for u in range(numsamples)])
v = vl + (vt*3.0)
print('正規＋右上がり', 'skew=', round(skew(v), 4), 'kurtosis=', round(kurtosis(v)))
plt.hist(v, bins=50, normed=True, color='black', alpha=0.5)
plt.grid()
plt.xlabel('x')
plt.ylabel('頻度')
plt.title('正規分布＋右上がり三角分布のヒストグラム')
plt.show()
