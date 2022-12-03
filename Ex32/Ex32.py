# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

def Random_list (length_list, down_border, up_border):
    '''
    Задаем список случайных целых чисел в диапазоне между down_border и up_border
    длиной length_list
    '''
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list

def Pairs_multiplication (source_list):
    '''
    Создаем список с произведениями пар чисел 
    (первый и последний, второй и предпосленний ... исходного списка 
    '''
    pairs_multiplication_list=[]
    length_list=len(source_list)
    for i in range(length_list//2+length_list%2):
        pairs_multiplication_list.append(source_list[i]*source_list[length_list-i-1])
    return pairs_multiplication_list

print()
number=int(input('Введите количество элементов списка (целое число более 1): '))
source_list=[]
resalt_list=[]
source_list=Random_list(number, -10, 10)
print('Исходный список')
print(source_list)
resalt_list=Pairs_multiplication(source_list)
print('Список произведений пар')
print(resalt_list)