# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

# БЫЛО


# lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  
# lst_2 = []
# lst_itog =[]
# for i in range(0,10):
#     lst_2.append(0)
# for i in lst:
#     lst_2[i]+=1    
# for i in range(0,len(lst_2)):
#     if lst_2[i] == 1:
#         lst_itog.append(i)
# print(lst_itog) 

# СТАЛО


lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]  
lst_itog = list(filter(lambda a: lst.count(a) == 1, lst))
print(lst_itog)
