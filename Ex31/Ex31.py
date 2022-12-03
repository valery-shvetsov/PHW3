# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# 

import random

def Random_list (lengh_list, down_border, up_border):
    '''
    Задаем список случайных чисел 
    '''
    rand_list=[]
    for i in range(0,lengh_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list

def Sum_odd_indexes (source_list):
    '''
    Считаем сумму элементов списка с нечетными индексами
    '''
    lengh_list=len(source_list)
    odd_indexes_sum=0
    for i in range(1,lengh_list,2):
        odd_indexes_sum=odd_indexes_sum+source_list [i]
    return odd_indexes_sum

print()
number=int(input('Введите количество элементов списка (целое число более 1): '))
source_array=[]
source_array=Random_list(number, -10, 10)
print('Исходный массив')
print(source_array)
sum=Sum_odd_indexes(source_array)
print()
print('Cумма элементов списка, стоящих на нечётной позиции: ', sum)
