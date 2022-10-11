# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.


n = 10
fib = [0, 1]
for i in range(n-1):
    fib.append(fib[-2] - fib[-1])

fib.reverse()

for j in range(n):
    fib.append(fib[-1] + fib[-2])

print(fib)   




# num_first = 0
# num_second = 1
# num = (int(input("ВВедите число: ")))
# for i in range(1,num):
#     temp = num_first
#     num_first = num_second
#     num_second = num_first + temp
#     print(num_first)



