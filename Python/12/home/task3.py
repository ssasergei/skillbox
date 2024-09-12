print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. 

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def summ_digital(num):
    summNum = 0
    while num > 0:
        summNum += num % 10
        num = num //10
    print('Сумма его цифр',summNum)


def min_digital(num):
    minNum = num % 10
    while num > 0:
        digital = num % 10
        if digital < minNum:
           minNum = digital
        num = num //10
    print('Минимальная цифра',minNum)

def max_digital(num):
    maxNum = num % 10
    while num > 0:
        digital = num % 10
        if digital > maxNum:
           maxNum = digital
        num = num //10
    print('Максимальная цифра: ',maxNum)

while True:
    number = int(input('Введите число: '))
    summ_digital(number)
    min_digital(number)
    max_digital(number)