"""
Рост взрослого населения города X имеет нормальное распределение.
Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
а). больше 182 см
б). больше 190 см
в). от 166 см до 190 см
г). от 166 см до 182 см
д). от 158 см до 190 см
е). не выше 150 см или не ниже 190 см
ё). не выше 150 см или не ниже 198 см
ж). ниже 166 см.
"""

from scipy.stats import norm
import numpy as np

data = np.arange(1, 10, 0.01)
pdf = norm.pdf(data, loc=174, scale=8)

# Za = (182-174)/8 = 1, Pa = 0,15866
Pa = 1 - norm(loc=174, scale=8).cdf(182)
print('a', Pa)

# Zb = (190-174)/8 = 2, Pa = 0,02275
Pb = 1 - norm(loc=174, scale=8).cdf(190)
print('б', Pb)

# Zv
upper_limit = norm(loc=174, scale=8).cdf(190)
lower_limit = norm(loc=174, scale=8).cdf(166)
Pv = upper_limit - lower_limit
print('в', Pv)

# Zg
upper_limit = norm(loc=174, scale=8).cdf(182)
lower_limit = norm(loc=174, scale=8).cdf(166)
Pg = upper_limit - lower_limit
print('г', Pg)

# Zd
upper_limit = norm(loc=174, scale=8).cdf(190)
lower_limit = norm(loc=174, scale=8).cdf(158)
Pd = upper_limit - lower_limit
print('д', Pd)

# Ze
upper_limit = norm(loc=174, scale=8).cdf(150)
lower_limit = 1 - norm(loc=174, scale=8).cdf(190)
Pe = upper_limit + lower_limit
print('e', Pe)

# Zeo
upper_limit = norm(loc=174, scale=8).cdf(150)
lower_limit = 1 - norm(loc=174, scale=8).cdf(198)
Peo = upper_limit + lower_limit
print('ё', Peo)

# Zj
lower_limit = norm(loc=174, scale=8).cdf(166)
Pj = lower_limit
print('ж', Pj)

# a 0.15865525393145707
# б 0.02275013194817921
# в 0.8185946141203637
# г 0.6826894921370859
# д 0.9544997361036416
# e 0.0241000299798093
# ё 0.0026997960632601965
# ж 0.15865525393145707
