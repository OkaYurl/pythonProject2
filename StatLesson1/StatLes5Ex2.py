"""
В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
значение с доверительной вероятностью 0,95.
"""

import scipy.stats as st
import numpy as np

data_set = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
p = 0.95
alpha = 1 - p
n = 10
v = n - 1
print(v)
data_s = data_set.mean()
print(data_s)
data_std = np.std(data_set, ddof=1)  # не сразу сообразила, что встроенная data_set.std() дает смещенное отклонение
print(data_std)
t = st.t.ppf(1 - alpha/2, v)
print('t', t)

T1 = data_s - t * data_std / np.sqrt(n)
T2 = data_s + t * data_std / np.sqrt(n)
print('доверительный интервал [', T1, T2, ']')

# 9
# 6.590000000000001
# 0.4508017549014448
# t 2.2621571627409915
# доверительный интервал [ 6.267515851415713 6.912484148584288 ]
