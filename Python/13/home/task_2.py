print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Python, чтобы остальным программистам стало проще работать. Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. Функция для нахождения максимума из двух чисел у него уже есть. Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); при этом она должна использовать для сравнений первую функцию maximum_of_two.

def maximum_of_two(num_1, num_2):
    maxNum = 0
    if num_1 > num_2:
        maxNum = num_1
    else:
        maxNum = num_2
    return maxNum
    

def maximum_of_three(num_1,num_2,num_3):
    maxNum = maximum_of_two(num_1,num_2)
    if num_3 > maxNum:
        maxNum = num_3
    return maxNum

number_1 = int(input('Введите число: '))
number_2 = int(input('Введите число: '))
number_3 = int(input('Введите число: '))
print(f'Максимальное число {maximum_of_three(number_1,number_2,number_3)} из чисел {number_1}, {number_2}, {number_3}')
