





k = 1
sum_ = 0
d = int(input("Введите колличество знаков после запятой: "))
for i in range(1000000):
    if i % 2 == 0:
        sum_ += 4/k
    else:
        sum_ -= 4/k
    k += 2
     
print(round(sum_,d))