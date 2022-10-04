#  Напишите программу, которая принимает на вход
#   число N и выдает набор  произведений чисел от 1 до N.


def Factorial (n):
    if n == 1:
        return n
    else:
        return n * Factorial(n-1)

num = int(input("Введите число:"))
for i in range(1,num +1):
    print(Factorial(i),end=" ")

# Вариант 2
# num = int(input("Введите число:"))
# factorial = 1
# for i in range(1,num + 1):
#     factorial *= i
#     print(factorial,end=" ")