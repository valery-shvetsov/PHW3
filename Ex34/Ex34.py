# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def Input_int(input_string):
    '''
    Ввод числа с пояснением
    '''
    while True:
        try:
            num=int(input(input_string))
            return num
        except ValueError:
            print('Введено не число. Давайте попробуем еще раз')

def Converting_decimal_to_binary (number:int):
    '''
    Преобразование десятичного целого числа в двоичное
    '''
    binary_number=[]
    while number!=0:
        binary_number.insert(0,number%2)
        number//=2
    decimal_number="".join(map(str,binary_number))
    return decimal_number

print()
number_10=Input_int('Введите целое десятичное число: ')
number_2=Converting_decimal_to_binary (number_10)
print (f' {number_10} в двоичной системе= {number_2}')


