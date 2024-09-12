print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
# написал две функции которые работают:
def gcd(num1, num2):
    print('наибольший общий делитель двух чиселnum1', num1, 'и', num2, end = ' ' )
    while num1 != 0 and num2 !=0:
        if num1 > num2:
            num1 = num1 - num2
        else: 
        # num1 < num2:
            num2 = num2 - num1
    print('равен',num1)

def nod_function(num1,num2):
    print('наибольший общий делитель двух чиселnum1', num1, 'и', num2, end = ' ' )
    while num1 != 0 or num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    print('равен',num1)

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
nod_function(number_1, number_2)
gcd(number_1,number_2)
