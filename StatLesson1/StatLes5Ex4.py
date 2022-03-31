"""
Продавец утверждает, что средний вес пачки печенья составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
"""

import scipy.stats as st
import numpy as np

mu0 = 200
n = 10
v = n - 1
data_set = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])
p = 0.99
alpha = 1 - p

# H0 mu=mu0
# H1 mu<>mu0
# T = 3,25
# Th = (mu - mu) / sigma / sqrt(n)

data_s = data_set.mean()  # mu
print(data_s)
data_std = np.std(data_set, ddof=1)  # sigma
print(data_std)
t = st.t.ppf(1 - alpha/2, v)
print('t', t)

th = (data_s - mu0) / (data_std / np.sqrt(n))
print('th', th)

if abs(th) < t:
    print('Гипотеза H0 верна')
else:
    print('Гипотеза H1 верна')

# 98.5
# 4.453463071962462
# t 3.2498355440153697
# th -1.0651074037450896
# Гипотеза H0 верна
