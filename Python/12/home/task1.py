
print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

def summa_n():
    number = int(input('Введите число: '))
    summNum = 0
    for num in range(number):
        num += 1
        summNum += num
    print('Я знаю, что сумма чисел от 1 до',number,'равна' ,summNum)

summa_n()