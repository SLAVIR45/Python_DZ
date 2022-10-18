# Вычислить число π c заданной точностью d

# БЫЛО

# from decimal import Decimal

# d = int(input("Введите желаемое колличество знаков после запятой:"))
# j = 1
# pi = 0
# for i in range (100000):
#     if i % 2 == 0:
#         pi += Decimal(4 / j)
#     else:
#         pi -= Decimal(4 / j) 
#     j += 2
# print(round(pi,d))


# СТАЛО
count = 1000
d = int(input("Введите желаемое колличество знаков после запятой:"))
pi_ = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(count))
print(round(pi_,d))
