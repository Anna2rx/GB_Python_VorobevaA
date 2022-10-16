print("Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.")
# Через строку нельзя решать.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11

digit = input("insert your number - \n")
digit = digit.replace(",", "")
digit = digit.replace(".", "")
need_digit = int(digit)
sum = 0
while need_digit != 0:
        sum += need_digit % 10
        need_digit = int(need_digit / 10)

print(sum)

print("Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N")#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(n: int):
    n_back = 1
    for el in range(1, n + 1):
        n_back *= el
    return n_back


number = int(input("insert your number - \n"))
list_of_number = []
for element in range(1, number + 1):
    list_of_number.append(factorial(element))

print(list_of_number)

print("Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой. Нельзя юзать find или count.")

# превая строка - "re"
# вторая строка, в которой ищем первую - "replace replacer"
# результат 2
str = input("insert str 1 - ")
str_two = input("insert str 2 -")

len_str = len(str)
len_str_two = len(str_two)
count = 0
for letter_two in range(len_str_two):
    if str[0] == str_two[letter_two]:
        for char in range(len_str):
            if letter_two + char < len_str_two:
                if str[char] != str_two[letter_two + char]:
                    break
            else:
                break
            if char + 1 == len_str:
                count += 1

print(count)


print("Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.")
def create_point(count: int):
    list_coord = []
    print("создание точки:")
    for el in range(count):
        list_coord.append(int(input(f"insert point coord {el + 1} - ")))
    return list_coord


def get_distance(f_p: list, s_p: list, count: int):
    sum = 0
    for coord in range(count):
        sum += pow(s_p[coord] - f_p[coord], 2)
    return pow(sum, 1/2)


n = int(input("insert your n -"))

first_point = create_point(n)
second_point = create_point(n)
print(get_distance(first_point, second_point, n))
