# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# БЫЛО
# from ipaddress import summarize_address_range


# lst = [2, 3, 5, 9, 3]
# print (lst)
# sum_ = 0
# for i in range(len(lst)):
#     if i % 2 == 1:
#         sum_ += lst[i]
# print(sum_)


# СТАЛО

lst = list(map(int, input("Введите числа через пробел: ").split()))
sum_ = [lst[i] for i in range(len(lst)) if  i % 2 == 1]
print(sum(sum_))
