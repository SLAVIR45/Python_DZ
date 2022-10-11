from decimal import Decimal
d = int(input("Введите желаемое колличество знаков после запятой:"))
j = 1
pi = 0
for i in range (100000):
    if i % 2 == 0:
        pi += Decimal(4 / j)
    else:
        pi -= Decimal(4 / j) 
    j += 2
print(round(pi,d))