# Задайте список из n чисел последовательности (1+1/n)^n
#  и выведите на экран их сумму,
# округлённую до трёх  знаков после точки.

# БЫЛО
# from pickle import APPEND

# n = int(input("Введите число:"))
# sum_ = 0
# list =[]
# for i in range(1,n+1):
#     list.append((1+1/i)**i)
# for j in range(len(list)):
#     sum_ += list[j]
# print(list)
# print(round(sum_,3))
# # print(round(sum(list),3)) # через функцию sum

# СТАЛО

n = int(input("Введите число:"))
list =[(1+1/i)**i for i in range(1,n+1)]
print(round(sum(list),3))
