print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225
def beard(word):
    beard = ''
    for symbol in word:
        beard = symbol + beard
    return beard 

firstNumber = input('Введите первое число: ')
secondNumber = input('Введите второе число: ')

print(f'Первое число наоборот: {beard(firstNumber)}')
print(f'Второе число наоборот: {beard(firstNumber)}')

summBeard = int(beard(firstNumber)) + int(beard(secondNumber))

print(f'Сумма: {summBeard}')

summBeardStr = str(summBeard)

print(f'Сумма наоборот: {beard(summBeardStr)}')

