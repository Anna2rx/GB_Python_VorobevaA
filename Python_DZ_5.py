print("1. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? Делаем игру против ботаа) Подумайте как наделить бота ""интеллектом""")
import random

# def print_turn(name, k, counter, left):
#   print(f"Ходит {name}, взял {k} конфет, теперь у него {counter} конфет, на столе осталось {left} конфет")
#
# sweets = 2021
#
# turn = random.randint(0, 2)
#
# player_counter = 0 # 0
# bot_counter = 0 # 1
#
# while sweets > 28:
#   if turn:
#     k = int(input("Введите количество конфет: "))
#     while k < 1 or k > 28:
#       k = int(input("Введите корректное (1-28) количество конфет: "))
#     player_counter += k
#     sweets -= k
#     turn = False
#     print_turn("Игрок", k, player_counter, sweets)
#   else:
#     k = random.randint(1, 29)
#     while sweets - k <= 28 and sweets > 29:
#       k = random.randint(1, 29)
#     bot_counter += k
#     sweets -= k
#     turn = True
#     print_turn("Бот", k, bot_counter, sweets)
# print("Победил игрок" if turn else "Победил бот")

print("2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы)")
from re import sub

def encode(text):
  return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), text)

def decode(text):
  return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), text)

mode = input("Выберите режим (e - кодирование, d - декодирование): ")
s = input("Введите строку: ")

if mode == 'e':
  print(encode(s))
elif mode == 'd':
  print(decode(s))
else:
  print("Некорректный режим")

print("задача 3. Напишите программу, удаляющую из текста все слова, содержащие абв.Функции FIND и COUNT юзать нельзя.")
import math
import re

my_string = "Алфавит начинается с абвг, не с бвабв"
print(my_string)
my_string = my_string.split(" ")
new_my_string = ""
for word in my_string:
    if re.sub(r'абв', r'', word) == word:
        new_my_string += word
        new_my_string += " "

print(new_my_string)

print("задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму. например, 5x^3 + 2x^2 + 6 и 7x^2+6x+3 , Тогда их сумма будет равна 5x^3 + 9x^2 + 6*x + 9")
def polynom_to_list(pol):
  pol_list = []
  index = 0
  for i in range(len(pol)):
    if pol[i] in ('+', '-'):
      pol_list.append(pol[index:i])
      index = i
  pol_list.append(pol[index:i+1])
  if pol_list[0] == '':
    pol_list.pop(0)
  if pol_list[0][0] not in  ('+', '-'):
    pol_list[0] = '+' + pol_list[0]
  return pol_list

def split_polynom(p):
  sign = p[0]
  p = p[1:]
  splitted = p.split('x')
  if (splitted[0] == ''):
    splitted[0] = '1'
  k = int(splitted[0])
  power = 0
  if len(splitted) > 1:
    power = int(splitted[1][1:]) if splitted[1] != '' else 1
  return [sign, k, power]

polynom1 = polynom_to_list(input("Введите первый многочлен: ").replace(' ', ''))
polynom2 = polynom_to_list(input("Введите второй многочлен: ").replace(' ', ''))

polynom1 = [split_polynom(p) for p in polynom1]
polynom2 = [split_polynom(p) for p in polynom2]

polynom_res1 = [p.copy() for p in polynom1]
polynom_res2 = [p.copy() for p in polynom2]

#print(polynom1)
#(polynom2)
for p in polynom_res1:
  terms = list(filter(lambda x: x[2] == p[2], polynom2))
  for t in terms:
    if t[0] == p[0]:
      p[1] += t[1]
    else:
      p[0] = p[0] if p[1] > t[1] else t[0]
      p[1] = abs(p[1]-t[1])

for p in polynom_res2:
  terms = list(filter(lambda x: x[2] == p[2], polynom1))
  for t in terms:
    if t[0] == p[0]:
      p[1] += t[1]
    else:
      p[0] = p[0] if p[1] > t[1] else t[0]
      p[1] = abs(p[1] - t[1])

polynom_res1.extend(list(filter(lambda x: x not in polynom_res1, polynom_res2)))
polynom_res1.sort(key = lambda x: x[2], reverse = True)
polynom_result = [f"{p[0]}{p[1] if p[1] != 1 or p[2] == 0 else ''}{'x^'+str(p[2]) if p[2] > 1 else 'x' if p[2] == 1 else ''}" for p in polynom_res1]
result = ''.join(polynom_result)
result = result if result[0] == '-' else result[1:]
print(result)