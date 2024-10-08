print('Задача 4. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).

# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.


# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n

# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10

# if first_num_count < 3:
#     print("В первом числе меньше трёх цифр.")
# else:
#     last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('Изменённое первое число:', first_n)
#     second_n = int(input("\nВведите второе число: "))
#     second_num_count = 0
#     temp = second_n
    
#     while temp > 0:
#         second_num_count += 1
#         temp = temp // 10
#     if second_num_count < 4:
#         print("Во втором числе меньше четырёх цифр.")
#     else:
#         last_digit = second_n % 10
#         first_digit = second_n // 10 ** (second_num_count - 1)
#         between_digits = second_n % 10 ** (second_num_count - 1) // 10
#         second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
#         print('Изменённое второе число:', second_n)
#         print('\nСумма чисел:', first_n + second_n)

    
def count_numbers(num):
    num_count  = 0
    while num > 0:
        num_count += 1
        num = num // 10
    return num_count

def change_number(num):
    last_digit = num % 10
    first_digit = num //10 ** (count_numbers(num) -1)
    between_digits = num %10 ** (count_numbers(num) -1) // 10
    num = last_digit * 10 ** (count_numbers(num) -1) + between_digits * 10 + first_digit
    return num

def main():
    while True:
        first_n = int(input("Введите первое число: "))
        if count_numbers(first_n) < 3:
          print("В первом числе меньше трёх цифр.")
        break
    while True:
        second_n = int(input("Введите второе число: "))
        if count_numbers(second_n) < 4:
            print("Во втором числе меньше четырёх цифр.")
        else:
            break

    print('\nИзменённое первое число: ', change_number(first_n))
    print('Изменённое второе число: ', change_number(second_n))

    change_summ = change_number(first_n) + change_number(second_n)
    print('\nСумма чисел:', change_summ)


main()