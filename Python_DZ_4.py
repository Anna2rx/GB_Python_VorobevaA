import random

print("задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
#решето Эрастофена
n = int(input("insert your N -"))
a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
        if n % a[i] != 0:
            a[i] = 0
    i += 1
a = set(a)
a.remove(0)
print(a)

print("задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.")

list_n = [1, 1, 4, 4, 5, 5, 6, 8, 8, 9, 9, 10]
print(list_n)
print(set(list_n))

print("задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.")

# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ax2 + bx + c = 0

k = 5
result = ""
for degree in range(k + 1):
    koef = random.randint(0, 100)
    if koef != 0:
        if degree < k - 1:
            result += f"{koef}*x^{k - degree} + "
        elif degree != k:
            result += f"{koef}*x + "
        else:
            result += f"{koef} + "
result = result[0:-2]
result += "= 0"
print(result)

print("задача 4 необязательная. Найдите корни квадратного уравнения, уравнение вводит через строку пользователь. например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.")

string = "3*x^2+5*x+2=0"
string = string.replace("+", "!")
string = string.replace("-", "!")
# string = str(string)
string = string.split("!")
print(string)
koef_a = 0
koef_b = 0
koef_c = 0

for el in string:
    if "^" in el:
        el = el.split("*")
        koef_a = int(el[0])
    elif "x" in el:
        el = el.split("*")
        koef_b = int(el[0])
    else:
        el = el.split("=")
        koef_c = int(el[0]) + int(el[1])

d = pow(koef_b, 2) - 4 * koef_a * koef_c
if d > 0:
    x1 = (-koef_b + pow(d, 0.5)) / (2 * koef_a)
    x2 = (-koef_b - pow(d, 0.5)) / (2 * koef_a)
    print(f"root one = {x1}, root two = {x2}")
elif d == 0:
    x = -koef_b / (2 * koef_a)
    print(f"root one = {x}")
else:
    print("The equation has no roots")

