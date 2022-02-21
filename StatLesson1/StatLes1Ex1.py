"""
Из колоды в 52 карты извлекаются случайным образом 4 карты.
    a) Найти вероятность того, что все карты – крести.
    б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
"""


import scipy.special as sc

ca1 = sc.comb(13, 4)  # число сомбинаций масть крести 4 из 13 возможных
ca2 = sc.comb(52, 4)  # всего возможных сочетаний 4 карт из 52
pa = ca1 / ca2
print("вероятность, что все карты - крести ", pa)

cb1 = sc.comb(48, 4)  # сочетаний без тузов
pb = (ca2 - cb1) / ca2  # сочетаний с тузами ко всем сочетаниям
print("вероятность, что среди 4-х карт хотя бы один туз", pb)
