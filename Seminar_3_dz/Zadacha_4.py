num = int(input("Введите число: "))
itog = ' ' 
while num > 0:
    itog = str(num % 2) + itog
    num //= 2
print (itog)  