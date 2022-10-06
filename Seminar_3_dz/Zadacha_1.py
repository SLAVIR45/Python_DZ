# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from ipaddress import summarize_address_range


lst = [2, 3, 5, 9, 3]
print (lst)
sum_ = 0
for i in range(len(lst)):
    if i % 2 == 1:
        sum_ += lst[i]
print(sum_)