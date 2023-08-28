# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста
# и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

n = int(input("Введите число N - кол-во кустов на грядке: "))
ai = int(input("Введите число ai - макс возможное число ягод на кусте: "))

dictionary = {}
for key in range(1, n + 1):
    value = randint(0, ai)
    dictionary[key] = value

print("Сгенерированная грядка:", dictionary)

max_berries = 0

for key in dictionary:
    curr_berries = dictionary[key] + dictionary.get(key - 1, 0) + dictionary.get(key + 1, 0)
    max_berries = max(max_berries, curr_berries)

print("Максимальное число ягод, которое можно собрать за 1 заход: ", max_berries)