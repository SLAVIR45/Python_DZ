# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите  произведение элементов на позициях a и b.

num = int(input("ВВедите N: "))
arr =[]
for i in range(-num,num + 1):
    arr.append(i)
print(arr) 
poz_1 = int(input("ВВедите позицию a: ")) - 1
poz_2 = int(input("ВВедите позицию b: "))  - 1 
temp_poz_1 = 0
temp_poz_2 = 0
for j in range(len(arr)):
    if j == poz_1:
        temp_poz_1 = arr[j]
    if j == poz_2:
        temp_poz_2 = arr[j]
print(f"произведение элементов на позициях  = {temp_poz_1 * temp_poz_2}")            
