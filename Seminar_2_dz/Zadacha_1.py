#  Напишите программу, которая  принимает на вход
#  вещественное число и показывает сумму его цифр.


num = input('Введите вещественное число формата х.хх: ')
sum = 0
for i in num:
    if i != '.':
            sum += int(i)
print(sum)