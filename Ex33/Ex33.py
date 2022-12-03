# 3-Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91\

import random
def Random_list (length_list, down_border, up_border):
    '''
    Задаем список случайных вещественных чисел в диапазоне между down_border и up_border
    длиной length_list
    '''
    random_float_list=[]
    for i in range(0,length_list):
        random_float_list.append(round(random.uniform(down_border, up_border), 4))
    return random_float_list

def Subtraction_frac_part (float_numbers_list):
    '''
    Находим максимальную и минимальную дробную часть 
    у элеменов массива и проводим их вычитание (max-min)
    '''
    max_min=0
    max_fract_part=0
    min_fract_part=1
    for i in range (len(float_numbers_list)):
        fract_part=round(float_numbers_list[i]%1,4)
        if fract_part>max_fract_part:
            max_fract_part=fract_part
        if fract_part<min_fract_part:
            min_fract_part=fract_part
    max_min=round(max_fract_part-min_fract_part,4)
    print('Максимальая дробная часть')
    print(max_fract_part)
    print('Минимальая дробная часть')
    print(min_fract_part)
    return max_min

print()
number=int(input('Введите количество элементов списка (целое число более 1): '))
source_list=[]
source_list=Random_list(number, -10, 10)
print('Исходный список')
print(source_list)
max_min_fract_part=Subtraction_frac_part(source_list)
print('Разность между максимальным и минимальным значением дробной части элементов')
print(max_min_fract_part)