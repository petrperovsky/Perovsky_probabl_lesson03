'''Устройство состоит из трех деталей.
Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
для второй - 0.2, для третьей - 0.25.
Какова вероятность того, что в первый месяц выйдут из строя:'''

Pall = 0.1 * 0.2 * 0.25  # все детали
P2 = 0.1 * 0.2 * 0.75 + 0.2 * 0.25 * 0.9 + 0.1 * 0.25 * 0.8  # только две детали
P1 = 0.1 * 0.8 * 0.75 + 0.2 * 0.9 * 0.75 + 0.25 * 0.9 * 0.8  # только одна деталь
P1_2 = P1 + P2  # одна или две
Pnone = 0.9 * 0.8 * 0.75  # ниодна
P1_2_3 = 1 - Pnone  # хотя бы одна

print(Pall, P2, P1_2, P1_2_3)

'''а). все детали = 0.005
б). только две детали = 0.080
в). хотя бы одна деталь = 0.45(9)
г). от одной до двух деталей? = 0.455'''
