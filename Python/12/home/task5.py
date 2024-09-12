print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text,number,letter):
    numberCount = 0
    letterCount = 0
    letterLower = letter.lower()

    for symbol in text:
        if symbol == number:
            numberCount += 1
        elif symbol == letter or symbol == letterLower:
            letterCount += 1
    print('Количество цифр',number,':', numberCount)
    print('Количество букв',letter,':', letterCount)


text =  input('Введите текст: ')
number = input('Какую цифру ищем? ')
letter = input('Какую букву ищём? ')

count_letters(text,number,letter)

