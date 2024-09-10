# task1
euro = int(input('Введеите сумму в евро: '))
dollor = float(euro * 1.25)
rub = round(float(dollor * 60.87),2)
print(euro, ' евро в рублях' , rub)

# task2
import math
seqNum = int(input('Введите кол-во чисел: '))

for number in range(seqNum):
    number = float(input('Введите число: '))
    if number >= 0:
        number = math.ceil(number)
        print('x = ',number, 'log(x)', end = '')
        number = math.log(number)
        print(number)
    else:
        number = math.floor(number)
        print('x = ',number, 'exp(x)', end = '')
        number = math.exp(number)
        print(number)

# task3
import math
fileSize = int(input('Укажите размер для скачивания: '))
speed = int(input('Какая скорость вашего соединения: '))
fileLoad = 0
sec = 0
percent = math.ceil((speed * 100) / fileSize)
percentCount = 0

while fileLoad < fileSize:
    fileLoad += speed
    percentCount += percent
    sec += 1
    if fileLoad > fileSize:
        fileLoad = fileSize
    if percentCount > 100:
        percentCount = 100
    print('Прошло',sec,'сек. Скачано',fileLoad,'из', fileSize,'МБ (',percentCount,'%)' )
    
# task4
nubmer = float(input('Введите число: '))
num = int((nubmer % 1) * 10)

print('Первая цифра после десятичной точки: ', num)

# task5
import math
planetRadios = float(input('Введите радиус случайной планеты: '))
earth = float(1.08321 * 10 ** 12)
plamerV = (4 * math.pi / 3 * (planetRadios ** 3))

if earth > plamerV:
    diff = round(earth / plamerV, 3)
    print('Объём палнеты Земля больше в ', diff,'раз')
else:
    diff = round(plamerV / earth, 3)
    print('Объём палнеты Земля меньше в ', diff,'раз')

# task6
import math
print('Введите местоположения коня')
horseX = float(input())
horseY = float(input())
print('Введите местоположения точки на доске')
pointX = float(input())
pointY = float(input())

squareHorseX = int (horseX * 10)
squareHorseY = int (horseY * 10)
squarePointX = int (pointX * 10)
squarePointY = int (pointY * 10)

print('Конь в клетке (',squareHorseX, ',', squareHorseY,'). Точка в клетке (',squarePointX, ',', squarePointY,').')
if abs(horseX - pointX) * (horseY - pointY) == 2:
    print ('Нет конь не может ходить в эту точку')
else:
    print ('Да конь может ходить в эту точку')

# task7
import math
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
more = int((number1 + number2) + abs(number1 - number2)) // 2
print('Наибольшее число: ', more)


