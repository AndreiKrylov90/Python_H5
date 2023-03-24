# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum_rec(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return  1 + 1 + sum_rec(a - 1, b - 1)
    
a = int(input("Напишите первое число "))
b = int(input("Напишите второе число "))
print(sum_rec(a, b))