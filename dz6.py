import numpy as np
import scipy.stats as stats

# задача 1
M = 80
n = 256
sigma = 16
z = 1.96
X1 = M-z*(sigma/np.sqrt(n))
X2 = M+z*(sigma/np.sqrt(n))
# P(78.04<M81.96)=0.95
print(X1, X2)
# задание 2
a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
# Поскольку из условия задачи нам ничего не известно ни о мат. ожидании генеральной совокупности ни о среднем квадратическом отклонении для генеральной совокупности,
# то для расчета доверительного интервала будем использовать t-критерий

print(f'Среднее выборочное: {np.mean(a): .2f},\n'
      f'Размер выборки n={len(a)},\n'
      f'Среднее квадратическое отклонение по выборке(несмещенное): {np.std(a, ddof=1): .2f}.'
      )


def t(confidens, len_array):
    alpha = (1-confidens)
    return stats.t.ppf(1-alpha/2, len_array-1)


print(
    f'Табличное значение t-критерия для 95%-го доверительного интервала данной выборки: {t(0.95, len(a)): .3f}')


def confidens_int(a, confidens):
    return round(np.mean(a)-t(confidens, len(a))*np.std(a, ddof=1)/len(a)**0.5, 3), \
        round(np.mean(a)+t(confidens, len(a))*np.std(a, ddof=1)/len(a)**0.5, 3)


print(
    f'95%-й доверительный интервал для истинного значения: {confidens_int(a, 0.95)}.')

# P(6.268<X<6.912)=0.95

# Задание 3

moth = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daug = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
df = 2*(len(moth)-1)

moth_mean = np.mean(moth)
daug_mean = np.mean(daug)
delta = moth_mean-daug_mean
print(
    f' средний рост матерей {moth_mean}  средний рост дочерей {daug_mean} дельта равна {delta}')

D1 = np.var(moth, ddof=1)
D2 = np.var(daug, ddof=1)  # аходим несмещенные дисперсии
D = (D1+D2)/2
print(D1, D2, D)

SE = np.sqrt(D/10+D/10)
print(SE)

t = stats.t.ppf(0.975, df)
print(f't равен {t}')

down = delta - (t*SE)
up = delta + (t*SE)
print(down, up)
# не понимаю какой вывод сделать их значений интервала -6.268418034506846 10.068418034506857
