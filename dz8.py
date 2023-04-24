import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import _tconfint_generic as t_stat
# Задача 1 
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array( [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
M_X = zp.mean()
M_Y = ks.mean()
M_XY = (zp * ks).mean()
cov_ks = M_XY - M_X * M_Y
# cov_ks 9157.84
print(cov_ks)
print(np.cov(zp, ks, ddof = 0)) #9157.84

cov_ks2 = ((zp - zp.mean()) * (ks - ks.mean())).mean()
print(cov_ks2)
std_X = zp.std()
std_Y = ks.std()
corr_ks = cov_ks / (std_X * std_Y)
print(corr_ks) #0.887
print(np.corrcoef(zp, ks)) #0.887

# задача 2 

x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
x_mean = x.mean()
x_std = x.std(ddof = 1)
x_mean_std = x_std / (np.sqrt(len(x)))
print(t_stat(x_mean, x_mean_std, len(x) - 1, 0.05, 'two-sided'))

# от 110,56  до 125,64

# Задача 3

x_mean = 174.2
x_std = np.sqrt(25)
x_mean_std = x_std / np.sqrt(27)
print(t_stat(x_mean, x_mean_std, 27 - 1, 0.05, 'two-sided'))

# от 172,22 до 176,18