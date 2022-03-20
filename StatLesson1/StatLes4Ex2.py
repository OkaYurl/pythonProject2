"""
О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
Если да, найдите ее.
"""

import numpy as np

a = 0.5
D = 0.2
b = np.sqrt(12 * D) + 0.5
M = (a + b) / 2
print('правая граница b', b, ' среднее значение', M)

# правая граница b 2.049193338482967  среднее значение 1.2745966692414834
