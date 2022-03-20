"""
Утверждается, что шарики для подшипников, изготовленные автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, если в выборке из n=100 шариков средний диаметр
оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.
"""

import scipy.stats as st
import numpy as np

mu0 = 17
mu = 17.5
D = 4
sigma = np.sqrt(D)  # критерий Z-тест
n = 100
alpha = 0.05

# H0 mu=mu0
# H1 mu>mu0
# Z = 1,95
# Zh = (mu - mu) / sigma / sqrt(n)
# Ph(Zh>Z)

Z = st.norm.ppf((1-alpha))
print('Z', Z)
Zh = (mu - mu0) / (sigma / np.sqrt(n))
print('Zh', Zh)

if abs(Zh) < Z:
    print('Гипотеза H0 верна')
else:
    print('Гипотеза H1 верна')

Pvalue = st.norm.sf(abs(Zh))
print('P-value', Pvalue)

if Pvalue < alpha:
    print('Гипотеза H1 верна')
else:
    print('Гипотеза H0 верна')

# Z 1.6448536269514722
# Zh 2.5
# Гипотеза H1 верна
# P-value 0.006209665325776132
# Гипотеза H1 верна
