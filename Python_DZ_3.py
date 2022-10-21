import math
import random

print("Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,стоящих на нечётной позиции.")
#
# *Пример:*
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
list = []
for _ in range(5):
    list.append(random.randint(0, 10))
print(list)
sum = 0
# range(x) - диапазон от 0 до Х-1
# range(z, x) - диапазон от Z до Х-1
# range(z, x, s) - диапазон от Z до Х-1 с шагом S
for index in range(1, len(list), 2):
    sum += list[index]
print(sum)

print("Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = []
final_list = []
for _ in range(5):
    list.append(random.randint(0, 10))
print(list)
len_list = len(list)
middle = len_list / 2
for el in range(math.ceil(middle)):
    final_list.append(list[el] * list[len_list - el - 1])
print(final_list)


print("Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")

# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_float = [1.1, 1.2, 3.1, 5, 10.01]
list_new = []
for el in list_float[1:]:
    new_el = round((el % 1), 2)
    if new_el != 0:
        list_new.append([new_el])
print(list_new)

minimum = float(''.join(map(str, min(list_new))))
maximum = float(''.join(map(str, max(list_new))))

print(f"max = {maximum},  min = {minimum} разница = {maximum - minimum}")


print("Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.")

# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = 45
str_double = ""
while number > 0:
    print(number)
    if number % 2 == 0:
        number = number // 2
        str_double += "0"
    else:
        number = number // 2
        str_double += "1"
str_double = str_double[:: -1]
print(str_double)

print("задача5 HARD необязательная. Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,причем чтоб количество элементов было четное...")

# Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое
# место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре,
# то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

m = int(input("insert your m -"))
n = int(input("insert your n -"))
list_random_digit = []
if m * n % 2 == 0:
    count_digit = m * n
else:
    count_digit = m * n + 1

for digit in range(count_digit):
    list_random_digit.append(random.randint(0, 9))

count = 1
count_delitel = 0
while count_delitel < 1:
    if count_digit % count == 0:
        count_delitel += 1
    count += 1

count_row = count
count_cel = int(count_digit / count)

print(list_random_digit)
for row in range(count_row):
    col_digit = []
    for col in range(count_cel):
        col_digit.append(list_random_digit[row * count_cel + col])
    print(col_digit)

print(list_random_digit)
for index in range(int(len(list_random_digit) / 2)):
    temp = list_random_digit[index]
    list_random_digit[index] = list_random_digit[len(list_random_digit) - index - 1]
    list_random_digit[len(list_random_digit) - index - 1] = temp
print(list_random_digit)


# m = int(input("insert m"))
# n = int(input("insert n"))
# len_arr = ((m * n) // 2) * 2
#
# arr = [random.randint(0, 100) for i in range(len_arr)]
#
#
# print(arr)