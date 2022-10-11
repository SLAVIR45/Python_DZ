import random

def random_ratio ():
    ratio = random.randint(0,100)
    return ratio


def random_sign ():
    num = random.randint(1,10)
    if num % 2 == 0:
        num = " + " 
    else: 
        num = " - "  
    return num


def random_k(k_):
    k_utf = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",} 
    for i in k_utf:
        if i == k_:
           return k_utf[i]

    



k =(input('Введите степень: '))
print (f"{random_ratio()}*x{random_k(k)}{random_sign()}{random_ratio()}*x = 0",end=" " )