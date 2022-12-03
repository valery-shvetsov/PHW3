# 5-Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

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

def Negafibonacci(number):
    '''
    Вывод ряда Негафибоначчи размером number чисел от 0
    '''
    negafibo=[0]
    negafibo_1=0
    negafibo_2=1
    k=1
    for i in range(1,number+1):
        fibo_sum=negafibo_1+negafibo_2
        negafibo_1=negafibo_2
        negafibo_2=fibo_sum
        negafibo.append(negafibo_1)
        negafibo.insert(0,negafibo_1*k)
        k*=-1
    return negafibo

print()
number_negafibo=Input_int('Введите количество чисел в ряду Негафибоначи (целое положительное число): ')
result_list=[]
print('Ряд Негафибоначчи для {a} элементов'.format(a = number_negafibo))
result_list=Negafibonacci(number_negafibo)
print(result_list)

