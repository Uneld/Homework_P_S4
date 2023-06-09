from random import randint

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# N = int(input("Введите размер первого массива: "))
# M = int(input("Введите размер второго массива: "))

# inputArray1 = [randint(1, N) for i in range(N)]
# inputArray2 = [randint(1, N) for i in range(M)]
# print(inputArray1)
# print(inputArray2)

# resSet = set()

# if len(inputArray1) > len(inputArray2):
#     for item in inputArray2:
#         if item in inputArray1:
#             resSet.add(item)
# else:
#     for item in inputArray2:
#         if item in inputArray1:
#             resSet.add(item)
# print(resSet)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,d
# находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input("Введите количество кустов: "))
inputArray1 = [randint(1, N) for i in range(N)]

sum = 0
for i in range(len(inputArray1)):
    # print(i, end=" ")
    if inputArray1[i - 2] + inputArray1[i - 1] + inputArray1[i] > sum:
        sum = inputArray1[i - 2] + inputArray1[i - 1] + inputArray1[i]
print(sum)
