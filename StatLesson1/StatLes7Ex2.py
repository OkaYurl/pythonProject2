"""
Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = 10


def mse_(b, y=y, x=x, n=10):
    return np.sum((b * x - y) ** 2) / n


alpha = 1e-6
b0 = 0
b = 0.1
i = 0
D = 1

while (D**2 >= 0.0000000001):
    D = alpha * (2 / n) * np.sum((b * x - y) * x)
    print(D)
    b -= D
    mse = mse_(b)

print('b=', b, 'mse=', mse)

plt.plot(x, y, 'o', label='original data')
plt.plot(x, b0 + b*x, 'r', label='fitted line')
plt.legend()
plt.show()

# b= 5.88947369810789 mse= 56516.86007188938
