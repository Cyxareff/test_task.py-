# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for j in range(c, d + 1):
#     print('\t', j, end=' ')
# print()
# for i in range(a, b + 1):
#     print(i, end="")
#     for j in range (c, d + 1):
#         print('\t', j * i, end='')
#     print()

# a, b, c, d, = map(int,input().split())
# for j in range(c, d + 1):
#     print('\t', j, end=' ')
# print()
# for i in range(a, b + 1):
#     print(i, end="")
#     for j in range (c, d + 1):
#         print('\t', j * i, end='')
#     print()

# a, b = (int(i) for i in input().split())
# s = 0
# count = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         s += i
#         count += 1
# print(s / count)

# genom = input().lower()
# g = genom.count('g')
# c = genom.count('c')
# print((g + c) / 10 * 100)

# s = input().lower()
# count = 0
# letter = s[0]
# for i in s:
#     if i == letter:
#        count += 1
#     else:
#         print(letter + str(count), end='')
#         count = 0
#         letter = i
#         count += 1
# print(letter + str(count))

# s = [int(i) for i in input().split()]
# b = []
# l = len(s)
# for i in range(l):
#     if l == 1:
#         print(*s)
#     elif i == 0:
#         b.append(s[-1] + s[1])
#     elif i == l - 1:
#         b.append(s[-2] + s[0])
#     elif  0 < i < l:
#         b.append(s[i - 1] + s[i + 1])
# print(*b)

# s = [int(i) for i in input().split()]
# s.sort()
# b = []
# for i in s:
#     if i == s[-1]:
#         break
#     elif i == i + i[+1]:
#         b.append(i)
# print(*b)

# s = [int(i) for i in input().split()]
# s.sort()
# l = len(s)
# b=[]
# for i in range(l - 1):
#     if s[i] == s[i + 1]:
#         if s[i] in b:
#             continue
#         else:
#             b.append(s[i])
# print(*b)

# a = int(input())
# b = a
# c = a ** 2
# while b != 0:
#     i = int(input())
#     b += i
#     c += i ** 2
# print(c)

# n = int(input())
# b = []
# for i in range(1, n + 1):
#     a = [i] * i
#     b += a
# for j in b[:n]:
#     print(j, end=' ')

# a = [int(i) for i in input().split()]
# x = int(input())
# if x in a:
#     for i in range(len(a)):
#         if x in a:
#             c = a.index(x)
#             print(c, end=' ')
#             a.remove(x)
#             a.insert(c, 999)
# else:
#     print('Отсутствует')

# from pprint import pprint
# n, m, k= (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(k):
#     rw, cl = (int(i) - 1 for i in input().split())
#     a[rw][cl] = - 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == - 1:
#                         a[i][j] += 1

# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

# pprint(a)

# from pprint import pprint

# n, m, = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[input() for j in range(m)] for i in range(n)]  # заполнение поля числами
# for i in range(n):
#     if i == n - 1:
#         print('end')
#         break
#     for j in range(m):
#         print(int(a[i][j]), end=' ')
#     print()

# a = [list(map(int, input().split())) for i in range(int(input()))]
# print(a)

# x = int(input())
# s = 510
# y = 45
# p = 10
# f = s + y * x + p * (x -1)
# print(f // 60, f % 60)


# a = int(input()) - 1
# b = ("январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь")
# if 0 > a or a >= 12:
#      print('Такого месяца не существует')
# elif 0 <= a <= 1 or 11 <= a <= 12:
#     print('зима')
# elif 1 <= a <= 4:
#     print('весна')
# elif 5 <= a <= 7:
#     print("лето")
# elif 8 <= a <= 11:
#     print("осень")

# s='абвгдеиклнопрстуцчья'
# b=int(input())
# if b==1:
#  print(s[-9],s[10],s[9],s[5],s[4],s[5],s[8],s[-2],s[9],s[6],s[7],sep='')
# elif b==2:
#  print(s[2],s[-6],s[10],s[-8],s[9],s[6:8],sep='')
# elif b==3:
#  print(s[-7],s[-8],s[5],s[4],s[0],sep='')
# elif b==4:
#  print(s[-3],s[5],s[-6],s[2],s[5],s[-8],s[3],sep='')
# elif b==5:
#  print(s[-9],s[-1],s[-6],s[9],s[6],s[-4],s[0],sep='')
# elif b==6:
#  print(s[-7],s[-5],s[1]*2,s[10],s[-6],s[0],sep='')
# elif b==7:
#  print(s[2],s[10],s[-7],s[7],s[-8],s[5],s[-7],s[5],s[9],s[-2],s[5],sep='')
#

# a, b, c = int(input()), int(input()), int(input())
# x = sorted([a, b, c])
# if x[0] + x[1] < x[2]:
#     print('0')
# elif x[0] == x[1] == x[2]:
#     print('3')
# elif x[0] == x[1] != x[2] or x[0] != x[1] == x[2]:
#     print('2')
# else:
#     print('1')

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print('високосный')
# else:
#     print('невисокосный')

# print(input().count('0'))


# a = int(input())
# if a % 10 == 0 or 11 <= a <= 19 or 5 <= a % 10 <= 9:
#         print('Мы нашли в лесу', a, 'грибов')
# elif a % 10 == 1:
#     print('Мы нашли в лесу', a, 'гриб')
# elif 2 <= a % 10 <= 4:
#     print('Мы нашли в лесу', a, 'гриба')

# n = int(input())
# for i in range(1, n + 1):
#     i = i ** 2
#     if i <= n:
#         print(i)


# a, b = int(input()), int(input())
# while a !=b:
#     a, b = max(a, b), min(a, b)
#     a = a - b
# print(a)

from pprint import pprint
# n = int(input())
# a = [[0 for j in range(n)] for i in range(n)]
# count = 1
# for i in range(n):
#     a[i] = count
#     count += 1
#     for j in range(n):
#         a[i][j] = count
#         count += 1
# pprint(a)

# from pprint import pprint
# n = int(input())
# a = []
# n1 = 0
# for i in range(n):
#     for j in range(0, n):
#         a.append(j)
        # if j == n:
        #     for k in range(n1, n - 1 - n1):
        #         n1 += 1
                # a.append(k)
# print(*a)

#
# n = int(input())
# a = [i for i in range(1, n + 1)]
# for j in a:
#     print(str(j) * j, end=' ')

# n = int(input()) # код выводит последовательность цифр увеличенную на само себя
# a = []
# for i in range(n + 1):
#     for j in range(i):
#         print(i, end=' ')
#         a.extend([i])
# print(a)
# for l in range(n + 1):
#     print(a[l], end=' ')

# n = int(input()) # код выводит последовательность цифр увеличенную на само себя
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])

# num, count =  1, 0 # код выводит последовательность цифр увеличенную на само себя
# for _ in range(int(input())):
#     print(num, end=' ')
#     count += 1
#     if num == count:
#         count = 0
#         num += 1
# #
# n = int(input()) # код выводит последовательность цифр увеличенную на само себя
# count = 0
# for i in range(n + 1):
#     if count < n:
#         for j in range(i):
#              if count < n:
#                 print(i, end=' ')
#                 count += 1
#              else:
#                  break
#     else:
#         break


# def beegeek(a, b): # функция которая возвращает распкованный список
#     c = []
#     d = []
#     for i in range(a, b + 1):
#         c.append(i)
#     for j in c:
#         if j % 3 == 0 and j % 7 == 0:
#             d.append('BeeGeek')
#         elif j % 3 == 0:
#             d.append('Bee')
#         elif j % 7 == 0:
#             d.append('Geek')
#         else:
#             d.append(j)
#     return print(' '.join([str(i) for i in d]))
# beegeek(14, 21)

#
# a, b = list(input()), list(input()) # Сравнение элементов двух списков
# c = []
# for i in b:
#     if i in a:
#         a.remove(i)
#         continue
#     else:
#         c.append(i)
# print(c[0])

# a = list(input())
# count = 0
# for i in a:
#     if i == '|':
#         print(1, end="")
#         a.pop(count + 1)
#         count += 1
#     elif i == '_' or  i == '¯':
#         print(0, end="")

# a = input() # выявление строки почти полиндром
# b = ''
# for i in a:
#     for j in range(ord('a'), ord('z') + 1):
#         if i == chr(j):
#             b += i
# for k in range(len(b) // 2):
#     if b[k] != b[-k-1]:
#         if b[k] != b[-k - 2]:
#             if b[k+1] != b[-k-1]:
#                 print('False')
#                 break
# else:
#     print('True')


# def q_sort(s): # карточная игра покер
#     if len(s) <= 1:
#         return s
#     elem = s[0]
#     left = list(filter(lambda x: x < elem, s))
#     center = [i for i in s if i == elem]
#     right = list(filter(lambda x: x > elem, s))
#     return q_sort(left) + center + q_sort(right)
#
# a = q_sort([int(x) for x in input().split()])
# count = 1
# count2 = 0
# count3 = 1
# for i in range(len(a) - 1):
#     if a[i] + 1 == a[i + 1]:
#         count3 += 1
#     if a[i] != a[i + 1]:
#         if count >= 2 and count2 >= 2:
#             break
#         elif count >= 2:
#             count2 = count
#             count = 1
#     elif a[i] == a[i + 1]:
#         count += 1
# if count3 == 5:
#     print('Стрит')
# elif count == 1 and count2 == 0:
#     print('Старшая карта')
# elif count == 4 or count2 == 4:
#     print('Каре')
# elif count == 2 and count2 == 3 or count == 3 and count2 == 2:
#     print('Фулл Хаус')
# elif count == 5:
#     print('Шулер')
# elif count == 1 and count2 == 3:
#     print('Сет')
# elif count == 2 and count2 == 0 or count == 1 and count2 == 2:
#     print('Пара')
# elif count == 2 and count2 == 2:
#     print('Две пары')
# print(count, count2)

# n = int(input())
# list = ''
# count = 1
# a = []
# for f in range(1,n +1):
#     for i in range(f):
#         a.append(count)
#         a.append(i)
#     a.reverse()
#     a.clear()
# print(list)

# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(n)] for i in range(n)]
# pprint(a)


# t_m = int(input())
# s_h = int(input())
# s_m = int(input())
# f_h = s_h + t_m // 60
# if f_h >= 24:
#     f_h = f_h % 24
# if t_m % 60 + s_m >= 60:
#     f_m = (t_m + s_m) % 60
#     f_h += 1
#     if f_h > 24:
#         f_h = f_h % 24
#         print(f_h, f_m)
#     print(f_h, f_m)
# else:
#     f_m = t_m % 60 + s_m
#     print(f_h, f_m)

# a = int(input())
# b = int(input())
# n = int(input())
# h = 0
# a_n = a * n
# b_n = b * n
# if b_n >= 60:
#     a_n += b_n // 60
#     b_n %= 60
# if a_n >= 60:
#     h += a_n //60
#     a_n %= 60
# print(h, a_n, b_n)

import math

# a = float(input())
# b = float(input())
# c = float(input())
# e = float(input())
# print(math.fsum((a, b, c, e)))

# a = int(input())
# key = 47
# print(a ^ key)

# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# if n1 == 255 == n2 and n3 == 255 == n4:
#     print('False')
# elif n1 == 0 == n2 and n3 == 0 == n4:
#     print('False')
# elif 0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255:
#     print('True')
# else:
#     print('False')

# day = {1 : 'пн', 2 : 'вт', 3 : 'ср', 4 : 'чт', 5 : 'пт', 6 : 'сб', 7 : 'вс'}
# if (n := int(input())) >= 7:
#     print(day[n % 7 + 1])
# else:
#     print(day[n + 1])

# a = input() # нахождение наименьшего числа
# b = input()
# c = input()
# d = a + b + c
# b = d[0]
# for i in d:
#     if int(i) > 0:
#         if int(i) < int(b):
#             b = i
#     else:
#         if int(i) < int(b):
#             b = i
# print(b)

# log = input()
# pas = input()
# if len(log) > 4 and len(pas) > 8 and log != pas:
#     print('True')
# else:
#     print('False')


# a = [i for i in input().split()]

# a = int(input()) # нахождение наименьшего числа
# b = int(input())
# c = int(input())
# if a >= b <= c:
#     print(b)
# elif b >= a >= c:
#     print(c)
# elif b >= a <= c:
#     print(a)

# command = "new_command"
# flag = "-f"
# argument = "hello"

# match command, flag:
#     case "print" | "write" | "say", "console":
#         print(argument)
#     case "decorate", _ as f:
#         print(f, argument)
#     case _:
#         print("error")

# a = input() # бот который отвечает на три вопрроса
# while a == 'Привет' or a == 'Как дела?' or a == 'Пока':
#     if a  == 'Привет':
#         print('Привет!')
#         a = input()
#     elif a == 'Как дела?':
#         print('Все классно!')
#         a = input()
#     elif a == 'Пока':
#         print('До скорой встречи!')
#         a = input()
# print('Прости, я еще не знаю таких фраз :(')

# framework = input()
# if framework == 'Flask' or framework == 'Django' or framework == 'Fast-API':
#     print('Python(',framework,'),Backend-dev', sep='')
# elif framework == 'Angular' or framework == 'React' or framework == 'Vue':
#     print('JavaScript/TypeScript(',framework,'),Frontend-dev', sep='')
# elif framework == 'Flutter' or framework == 'React Native':
#     print('JavaScript(',framework,'),Cross-Mobile-dev', sep='')
# elif framework == 'Pandas' or framework == 'skit-learn' or framework == 'keras':
#     print('Python(',framework,'),Data-Scientist', sep='')
# else:
#     print("модель еще не обучена")

# n = int(input()) # нахождение факториала числа
# count = 2
# b = 1
# for i in range(1, n):
#     b  *= count
#     count += 1
# print(b)

# n = int(input()) # нахождение факториала числа
# res = 1
# for i in range(1, n):
#     res *= (i + 1)
# print(res)

# for i in range(1, 10):
#     # 9 раз выполни код ниже
#     for j in range(1, 10):
#         # 9 раз выполни команду ниже
#         print(i*j, end=' ')
#     print()

# n = int(input()) # треугодьник Паскаля обход соседних клеток с верху в низ с лева на право
# a = []
# for i in range(n + 1):
#     a.append([1] + [0] * n)
# for i in range(1, n + 1):
#     for j in range(1, i +1):
#         a[i][j] =  a[i-1][j] + a[i - 1][j - 1]
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print(a[i][j], end ='')
#     print()

# x = int(input())
# res = 1
# while x  != 0:
#     res *= x
#     x = int(input())
# print(res)

# res = 1
# while (x := int(input())) != 0:
#     res *= x
# print(res)

# n = int(input()) # перевод числа из 10ой системы в 5ую
# a = []
# if n == 0:
#     print(n)
# else:
#     while n % 2 != 0 or n // 2 > 0:
#         a.append(n % 2)
#         n //= 2
#     a.reverse()
#     print(*a, sep='')

# n1, n2, n3, n4 = [int(i) for i in input().split('.')] # Не решенная задача!!!!!
# a = []
# b = []
# for i in [n1, n2, n3, n4]:
#     if i == 0:
#         b.append(i)
#     else:
#         while i % 2 != 0 or i // 2 > 0:
#             a.append(i % 2)
#             i //= 2
#         a.ljust(8 - len(a), '0')
#         a.reverse()
#         b += a
#         a.clear()
# print(b, sep='', end='')
# + 0 * (8 - len(str(i % 2)))
# n = len(b)
# print(type(b))
# for i in range(n - 1):
#     print(type(b[i]), b[i])
#     if b[i] == 0 and b[i + 1] == 1:
#         a.append('False')
#     else:
#         a.append('True')
# if False in a:
#     print('False')
# else:
#     print('True')
# print(a)




# command = input().split()
# list_command = ['add', 'exit', 'minus', 'mul', 'div', 'result', 'zero']
# count = 0
# while command[0] != 'exit':
#     if command[0] in list_command:
#         if command[0] == 'zero':
#             count = 0
#             command = input().split()
#         elif command[0] == 'add':
#             count += int(command[1])
#             command = input().split()
#         elif command[0] == 'minus':
#             count -= int(command[1])
#             command = input().split()
#         elif command[0] == 'mul':
#             count *= int(command[1])
#             command = input().split()
#         elif command[0] == 'div':
#             if command[1] == '0':
#                 break
#             else:
#                 count //= int(command[1])
#                 command = input().split()
#         elif command[0] == 'result':
#             print(count)
#             command = input().split()
#     else:
#         break

# s = input()
# if s.isnumeric() == True:
#     print(int(s) * 3)
# else:
#     print('не число')

# s = input()
# for i in range(len(s)):
#     print(s[i] * (i + 1))

# s = input()
# print(s[1] * 4)
# print(s[-2:] + '!')
# print(s[:-3])
# print(s[:] + s[::-1])
# print(s[1::2])
# print(s[::2])

# s = input() # Шифр Цезаря
# step = int(input())
# for i in s:
#     if ord(i) + step >122:
#         print(chr(ord(i) + step - 122 + ord('a') - 1), end='')
#     else:
#         print(chr(ord(i) + step), end='')

# s = input() # дешифратор шрифра Цезаря
# step = int(input())
# for i in s:
#     if ord(i) - step < 97:
#         print(chr(ord('z') + 1 - (97 - (ord(i)- step))), end='')
#     else:
#         print(chr(ord(i) - step), end='')

# my_str = input() #  наибольшее количество подряд идущих одинаковых символов
# last_char = ''
# current_seq_len = 0
# max_seq_len = 0
# max_char = ''
# for c in my_str:
#     if c == last_char:
#         current_seq_len += 1
#         if current_seq_len >= max_seq_len:
#             max_seq_len = current_seq_len
#             max_char = last_char
#     else:
#         current_seq_len = 1
#         last_char = c
# if max_seq_len == 0:
#     print(last_char)
#     print(current_seq_len)
# else:
#     print(max_char)
#     print(max_seq_len)


# n= float(input()) #округление числа до второй цифры после точки при момощи f" - строки
# print(f"{n:.2f}")


# nums = [int(i) for i in input().split(' ')] #сложение соседних чисел
# count = 0
# for i in range(len(nums) - 1):
#     count = int(nums[i]) + int(nums[i + 1])
#     print(count, end=' ')
#     count = int(nums[i])

# nums = [int(i) for i in input().split(' ')] # нахождение второго по максимальности числа
# a = list(set(nums))
# a.remove(max(a))
# print(max(a))

# nums = [int(i) for i in input().split(' ')] # перенос всех нулеи в конец списка
# zero = []
# num = []
# for i in nums:
#     if i == 0:
#         zero.append(i)
#     else:
#         num.append(i)
# print(*(num + zero), sep=' ')

# nums = [int(i) for i in input().split(' ')] # удаление всех не четных из списка
# for i in nums:
#     if i % 2 == 0:
#         print(i, end=' ')

# nums = [int(i) for i in input().split(' ')] # нахождение медианы списка чисел
# a = sorted(nums)
# if len(a) % 2 == 1:
#     print(a[int((len(a) - 1) // 2)])
# elif len(a) % 2 == 0:
#     if (a[len(a) // 2] + a[len(a) // 2 - 1]) % 2 == 0:
#         print((a[len(a) // 2] + a[len(a) // 2 - 1]) // 2)
#     else:
#         print((a[len(a) a = int(input())
# b = []
# while a != 0:
#     if a not in b:
#         b.append(a)
#         a = int(input())
#     else:
#         a = int(input())
# b.append(0)
# print(len(b))// 2] + a[len(a) // 2 - 1]) / 2)

# a = int(input()) # определение уникальных чисел в последовательности
# b = []
# while a != 0:
#     if a not in b:
#         b.append(a)
#         a = int(input())
#     else:
#         a = int(input())
# b.append(0)
# print(len(b))

# a = (int(i) for i in input().split(' ')) #сумма квадратов последовательности
# b = 0
# for i in a:
#     b += i ** 2
# print(b)

# a = input() # множества и пользователский ввод данных
# b = input()
# c = input()
# required = set()
# optional = set()
# user_data = set()
# required.update(a.split())
# optional.update(b.split())
# user_data.update(c.split())
# if user_data <= required:
#     print(required | optional >= user_data)
# else:
#     print(False)


# a = input().split(' ') # Работа по формированию словаря и его сортировка словаря
# letter = {}
# count = 0
# for i in a:
#     if i in letter:
#         continue
#     else:
#         letter[i] = a.count(i)
# for key, value in sorted(letter.items()):
#     print(key, value)


#[{"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 50},"age": 22}, {"id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 62},"age": 80}]
# import json  # работа с библиотекой json и масивом множества джля выяснения возраста
# d = json.loads(input())
# count = 0
# for i in range(len(d)):
#     if count <= d[i]['chief']['age'] >= d[i]['age']:
#         count = d[i]['chief']['age']
#     else:
#         if count <= d[i]['age']:
#             count = d[i]['age']
#         else:
#             continue
# print(count)

# a = list(input().split('/'))
# b = list(input().split('/'))
# print(a, b)

# a = int(input()) # вывод последовательности числе в обратном порядке без учета -1
# b = []
# while a != -1:
#     b.append(a)
#     a = int(input())
# for i in b[::-1]:
#     print(i)

# command = input().split()
# a = []
# while command[0] != 'close':
#     if command[0] == 'add':
#         a.append(command[1])
#         command = input().split()
#     elif command[0] == 'pop':
#         print(a.pop(0))
#         command = input().split()
#     elif command[0] == 'head':
#         print(a[0])
#         command = input().split()

# command = [int(i) for i in input().split()]
# while 'end' not in (c :=input().split()):
#     if c[0] == 'insert':
#         command.append(int(c[1]))
#     elif c[0] == 'pop':
#         command.sort()
#         print(command.pop())
#
# count = 0
# m = 10
# while m > 0:
#    if(x:= int(input())) % 2== 0:
#        count += 1
#        m -= 1
#    else:
#        m -=1
# if count == 10:
#     print('YES')
# else:
#     print('NO')

# n = int(input()) # последовательность Фибоначи
# fb1 = 1
# fb2 = 1
# if n < 2:
#     print(1)
# else:
#     print(fb1, fb2, end=' ')
#     while n - 2  > 0:
#         summ = fb1 + fb2
#         fb1 = fb2
#         fb2 = summ
#         print(fb2, end=' ')
#         n -= 1

# i = int(input())
# sum = 0
# while i != 0:
#    if i - 25 >= 0 and i - 25 <= 25 or i - 25 >= 25:
#       sum += 1
#       i = i - 25
#    elif i - 25 < 0:
#       if i - 10 >= 0 and i - 10 <= 10 or i - 10 >= 10:
#          sum += 1
#          i = i - 10
#       elif i - 10 < 0:
#          if i - 5 >= 0 and i - 5 <= 5 or i - 5 >= 5:
#             sum += 1
#             i = i - 5
#          elif i - 5 < 0:
#             if i - 1 >= 0 and i - 1 <= 1 or i - 1 >= 1:
#                sum += 1
#                i = i - 1
# print(sum)

# num = input()
# a = num[-1]
# count = 0
# for i in num[::-1]:
#     if i >= a:
#         count += 1
#         a = i
# if len(num) == 1:
#     print('YES')
# elif len(num) == count:
#     print('YES')
# else:
#     print('NO')

# mx = -1
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx or mx == 0:
#             mx = x
# if s != 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# n = int(input()) # Равнобедренный треугольник из "*"
# for i in range(1, 3):
#     if i == 1:
#         for j in range(1, (n + 1) // 2 + 1):
#             print('*' * j)
#     else:
#         for j in range(1, (n + 1) // 2):
#             print('*' * ((n + 1) // 2 - j))

# n = int(input()) # треугольник из чисел
# for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print( i, end='')
#         print()

# n = int(input()) # численный треугольник
# a = 0
# for i in range(1, n + 1):
#     for j in range(i):
#         a += 1
#         print(a, end='')
#     print()

# n = int(input()) # численный треугольник с обратной последовательностью
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(j - 1, 0, -1):
#         print(k, end='')
#     print()

# a = int(input()) # нахождение максимальной суммы делителей числа
# b = int(input())
# sum1 = 0
# max_sum = 0
# number = 0
# for i in range(a, b + 1):
#     count = 0
#     sum1 = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             sum1 += j
#     if sum1 >= max_sum :
#         max_sum = sum1
#         number = i
# print(number, max_sum)

# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#
#     print(i, '+' * count, sep='')
#     count = 0

# n = input() # Цифровой корень числа
# a = 0
# if len(n) <= 1:
#     print(n)
# else:
#     while len(n) != 1:
#         for i in range(len(n)):
#             a += int(n) % 10
#             n = str(int(n) // 10)
#         if len(str(a)) > 1:
#             n = str(a)
#             a = 0
#         else:
#             print(a)

# n = int(input()) # сумма фактриалов числа
# fact = 1
# sum_fact = 0
# for i in range(n):
#     fact *= (i + 1)
#     sum_fact += fact
# print(sum_fact)

# a = int(input())
# b = int(input())
# count = 0
# for i in range(a, b + 1):
#     if i <= 1:
#         continue
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)
#     count = 0


# n = int(input()) # звездная рамка ******
# a = n
# while n > 0:
#     if n == 1:
#         print('*' * 19)
#     elif n == a:
#         print('*' * 19)
#     else:
#         print('*', ' ' * 15, '*')
#     n -= 1

# n = input()
# print(n.count('3'))
# count = 0
# count1 = 0
# sum_5 = 0
# multip = 1
# count2 = 0
# for i in n:
#     if i == n[-1]:
#         count += 1
# print(count)
# for i in n:
#     if int(i) % 2 == 0:
#         count1 += 1
# print(count1)
# for i in n:
#     if int(i) > 5:
#         sum_5 += int(i)
# print(sum_5)
# for i in n:
#     if int(i) > 7:
#         multip *= int(i)
# if multip >= int(i):
#     print(multip)
# else:
#     print(1)
# for i in n:
#     if int(i) == 5:
#         count2 += 1
#     elif int(i) == 0:
#         count2 += 1
# print(count2)

# s = input().lower()
# countg = 0
# counts = 0
# for i in range(len(s)):
#     if s[i] in 'ауоыиэяюёе':
#         countg += 1
#     elif s[i] in 'бвгджзйклмнпрстфхцчшщ':
#         counts += 1
# print('Количество гласных букв равно', countg)
# print('Количество согласных букв равно', counts)

# n = int(input()) # перевод числа из 10ой системы в 2ую
# a = []
# if n == 0:
#     print(n)
# else:
#     while n % 2 != 0 or n // 2 > 0:
#         a.append(n % 2)
#         n //= 2
#     a.reverse()
#     print(*a, sep='')

# s = input() # Строка Полиндром
# if len(s) % 2 == 0:
#     if s[:int(len(s))// 2] == s[:int(len(s))  // 2 - 1: -1]:
#         print('YES')
#     else:
#         print('NO')
# else:
#     if s[:(int(len(s)) - 1) // 2] == s[:(int(len(s)) - 1) // 2: -1]:
#         print('YES')
#     else:
#         print('NO')

# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])

# s = input() # Строка Полиндром
# if len(s) % 2 == 0:
#     print(s[int(len(s)) // 2:] + s[:int(len(s))// 2])
# else:
#     print(s[int(len(s)) // 2 + 1:] + s[:int(len(s)) // 2 + 1])
#


# s = input().split()
# if s[0][0] == s[0][0].upper() and s[1][0] == s[1][0].upper():
#     print('YES')
# else:
#     print('NO')

# s = input().lower()
# if 'хорош' in s:
#     print('YES')
# else:
#     print('NO')

# s = input()
# count = 0
# for i in s:
#     if i in 'abcdefghijklmnopqrstuvwxyz':
#         count += 1
# print(count)
#
# s = input().lower()
# print('Аденин:', s.count('а'))
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))

# n = int(input())
# count = 0
# while n > 0:
#     s = input()
#     if s.count('11') >= 3:
#         count +=1
#     n -= 1
# print(count)

# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# s = input() #Самый частотный символ в строке
# count = 0
# char = ''
# for i in range(len(s)):
#     if s.count(s[i]) >= count:
#         count = s.count(s[i])
#         char = s[i]
# print(char)

# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') > 1:
#     print(s.find('f'), s.rfind('f'))
# else:
#     print('NO')

# s = input()
# print(s[:s.find('h')] + s[s.rfind('h') + 1:])

# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# year = 2010
# many = '10k'
# name_many = 'Bitcoin'
# print('In {0}, someone paid {1} {2} for two pizzas.'.format(year, many, name_many))

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

# for i in range(26):
#     print(chr(ord('A') + i))

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# s = input()
# for i in s:
#     print(ord(i), end=' ')

# step = int(input()) # декодирование шифра Цезаря
# s = input()
# for i in s:
#     if ord(i) - step < 97:
#         print(chr(ord('z') + 1 - (97 - (ord(i)- step))), end='')
#     else:
#         print(chr(ord(i) - step), end='')

# s = input() # Второе вхождение символа f в строку
# if s.count('f') >= 2:
#     s = s.replace('f', 'a', 1)
#     print(s.find('f'))
# elif s.count('f') == 1:
#     print(-1)
# else:
#     print(-2)

# s = list(input()) # Удаляет все кратные 3 символы из строки
# del s[0::3]
# print(*s, sep='')

# s = input() # Код меняет порядок символов в строке, между двумя символами 'h' разворачвая их задом на перед
# a = s[s.find('h') + 1:s.rfind('h')]
# print(s[:s.find('h') + 1]  + a[::-1] + s[s.rfind('h'):])

# s = [] #Поисковые запросы в списке
# s_zapros = []
# s_final = []
# count = 0
# for i in range(int(input())):
#     s.append(input())
# for k in range(int(input())):
#     s_zapros.append(input().lower())
# for j in s:
#     count = 0
#     for l in s_zapros:
#         if l.lower() in j.lower():
#             count += 1
#             if count == len(s_zapros):
#                 s_final.append(j)
# print(*s_final, sep='\n')

# s = [] #Сортировка списка цифр
# s_final = []
# for i in range(int(input())):
#     s.append(int(input()))
# count = len(s)
# while  count > 0:
#     for j in s:
#         if j < 0:
#             s_final.append(j)
#             count -= 1
#     for j in s:
#         if j == 0:
#             s_final.append(j)
#             count -= 1
#     for j in s:
#         if j > 0:
#             s_final.append(j)
#             count -= 1
# for k in s_final:
#     print(*k, sep='\n')


# n = input().split('.') #Проверка коректности IP адреса
# count = 0
# for i in n:
#     if 0 <= int(i) <= 255:
#         count += 1
# if count == len(n):
#     print('ДА')
# else:
#     print('НЕТ')

# n = input() # Добавить разделитель в строку
# y = input()
# s = []
# for i in n:
#     s.append(i)
# print(y.join(s))

# n = input().split() #Количество совпадающих пар
# count = 0
# for i in range(len(n) - 1):
#     for j in range(i + 1, len(n)):
#         if n[i] == n[j]:
#             count += 1
# print(count)

# numbers = [8, 9, 10, 11]
# numbers.pop(1)
# numbers.insert(2, 17)
# numbers.extend([4, 5, 6])
# numbers.pop(0)
# numbers.extend(numbers.copy())
# numbers.insert(3, 25)
# print(numbers)

# n = [int(i) for i in input().split()] #Меняем местами макс и мин значения в списке
# a = n.index(max(n))
# b = n.index(min(n))
# n[b], n[a] = n[a], n[b]
# print(*n)

# n = input().lower().split()
# print('Общее количество артиклей:', n.count('a') + n.count('an') + n.count('the'))

# n = input().split('#') # Удаление комментариев в строках
# a = int(n[1])
# b = ''
# for i in range(a):
#     b = input()
#     if '#' in b:
#         print(b[:b.index('#')].rstrip())
#     else:
#         print(b)

# n = input().split() # Сортировка списка цифр с переводом в int
# for i in range(len(n)):
#     n[i] = int(n[i])
# n.sort()
# print(*n)
# n.sort(reverse = True)
# print(*n)