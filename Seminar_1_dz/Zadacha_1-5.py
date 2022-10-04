# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и  проверяет, является ли этот день  выходным.


print("Enter number")
num = int(input())
if num == 6 or num == 7:
    print(f"{num}  Weekend")
elif num >= 1 and num <=5:
    print(f"{num} Working day")
else: 
    print(f"{num} is not a number of the week")



    # Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех  значений  предикат.


x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)


 # Напишите программу, которая принимает на вход координаты  точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в  которой находится эта точка


x = int(input('Введите x: '))
y = int(input('Введите y: '))
if x > 0 and y > 0:
    print("1 четверть")
elif x < 0 and y > 0:
    print("2 четверть")
elif x < 0 and y < 0:
    print("3 четверть")
elif x > 0 and y < 0:
    print("4 четверть")        
else:
    print("точка находится на оси координат")    



    # Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат  точек в этой  четверти (x и y).

number = int(input('Введите четверть: '))

if number < 1 or number > 4:
    print("четверти не существует")
elif number < 1 or number > 4:
    print("четверти не существует")    
elif number == 1:
    print("x > 0 , y > 0")
elif number == 2:
    print("x < 0 , y > 0")
elif number == 3:
    print("x < 0 , y < 0")
elif number == 4:
    print("x > 0 , y < 0")       


 # Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между  ними в 2D  пространстве.


from cmath import sqrt


print('введите координату A')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("введите координату B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))
print('Расстояние между точками А и В ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))                