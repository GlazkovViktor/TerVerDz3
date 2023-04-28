
import scipy.stats as stats
import numpy as np


football_players=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey_players=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifters=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
alpha=0.05
# Проверим данные на нормальность распределения

print(stats.shapiro(football_players))
print(stats.shapiro(hockey_players))
print(stats.shapiro(weightlifters))

# P-value для каждой выборки больше альфа принимаем, что данные распределены нормально.

# Проверим равенство дисперсий.

print(stats.bartlett(football_players, hockey_players, weightlifters))
# P-value для каждой выборки больше alpha принимаем, что дисперсии равны.


#  Нулевая:различия среднего роста среди взрослых футболистов, хоккеистов и штангистов нет
#  Первая: различия среднего роста среди взрослых футболистов, хоккеистов и штангистов есть

print(stats.f_oneway(football_players, hockey_players, weightlifters))
# Получили значение на уровне p-value = 0.01048 статистической значимости alpha= 0.05  значит отвергаем нулевую гипотезу.
# Средний рост футболистов, хоккеистов и штангистоа различен.