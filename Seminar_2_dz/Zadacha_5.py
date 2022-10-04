#  Реализуйте  алгоритм перемешивания списка.
import random

num = int(input("ВВедите N: "))
arr = [ ]
for i in range(num):
    arr.append(random.randint(1,100))
print(arr)    
arr_p = [ ]
for j in range(len(arr)):
    temp = arr[j]
    rand = random.randint(j,len(arr)-1) 
    arr[j] = arr[rand]
    arr[rand] = temp
    arr_p.append(arr[j])
print(arr_p)    