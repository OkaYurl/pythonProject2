"""
Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
для второй - 0.2, для третьей - 0.25.
Какова вероятность того, что в первый месяц выйдут из строя:
а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
"""

p1 = 0.1
q1 = 1 - p1
p2 = 0.2
q2 = 1 - p2
p3 = 0.25
q3 = 1 - p3

P1 = p1*p2*p3
print('a', P1)

P2 = p1*p2*q3 + p1*q2*p3 + q1*p2*p3
print('б', P2)

P3 = 1 - q1*q2*q3
print('в', P3)

P4 = P3 - P1
print('г', P4)

# 0.005000000000000001
# б 0.08000000000000002
# в 0.45999999999999996
# г 0.45499999999999996