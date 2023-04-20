import numpy as np
import scipy.stats as stats

#Задание 1
A=np.array([380,420, 290])
B=np.array([140,360,200,900])

print(stats.mannwhitneyu(A,B))
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286) Следовательно различий нет

#Задание 2

X1 = np.array([150, 160, 165, 145, 155])
X2 = np.array([140, 155, 150, 130, 135])
X3 = np.array([130, 130, 120, 130, 125])

print(stats.friedmanchisquare(X1,X2,X3))
# FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441) 
# нулевая теория отвергается, значит различия есть 

#Задание 3 

X4 = np.array([150, 160, 165, 145, 155])
X5 = np.array([140, 155, 150, 130, 135])
print(stats.wilcoxon(X4,X5))
# WilcoxonResult(statistic=0.0, pvalue=0.0625) нулевая теория неотвергатеся, различий нет 

# Задание 4
Phelps1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
Phelps2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
Phelps3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
print(stats.kruskal(Phelps1,Phelps2,Phelps3))

#KruskalResult(statistic=5.465564058257224, pvalue=0.06503809985904942)
# Нулевая не отвергается , различий нет

# Задание 5

X = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])

mean = X.mean()
std = X.std(ddof=1)

t_fact = (mean - 2.5) / std * np.sqrt(len(X))
print(t_fact)
#0.563061366180296
#По таблице для критерия Стьюдента находим t = 1.833 (для = 0.05 и 9 степенями свободы).
#Так как t > t_fact (1.833 > 0.56), то гипотеза верна и изделия соответствуют заявленному размеру.

n = 10
m = 2.5

t1 = stats.t.ppf(0.975, 9)
print(f"t теор = {t1:.2f}")

t2 = (mean - m) * np.sqrt(n) / std
print(f"t рассч = {t2:.3f}")
#t теор = 2.26
#t рассч = 0.563
#так как t теор > t рассч, считаем что нулевая гипотеза верна

