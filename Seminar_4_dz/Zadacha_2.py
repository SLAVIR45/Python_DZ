# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input("Введите число: "))
lst =[ ]
for i in range(2,num):
    if num % 2 == 0:
        lst.append(2)
        num /= 2
    else:
        if num % i == 0:
            lst.append(i)
            num /= i
print(lst)    



    
