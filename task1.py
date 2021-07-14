import re

# Введення рядку користувачем
str = input("Введіть рядок: ")
# Знаходження чисел у заданому рядку
rd = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
rd = [int(i) for i in rd]
# Виведення відформатного рядку
print("Рядок без чисел:\n", str, sep='')


# Функція заміни букв за умовою
def function(str):
    str, result = str.title(), ""
    for slovo in str.split():
        result += slovo[:-1] + slovo[-1].upper() + " "
    return result[:-1]

# Виведення слів після форматування
print("\nСлова змінені за вказаною умовою:\n", function(str), sep='')
# Виведення масиву чисел
print("Масив чисел з рядка:\n", rd, sep='')

# Знаходження макс. числа за умови наявності чисел у введеному рядку і вихід з програми у разі їх відсутності
if rd:
    maxNum = max(rd)
    index = rd.index(maxNum)
    print("\nМаксимальне число:", maxNum)
if not rd:
    print("Рядок не містить чисел!")
    exit()
    
# Запис масиву чисел піднесених до степеня
arr = []
for i in range(len(rd)):
    if rd[i] != max(rd):
        arr.append(pow(rd[i], i))
# Виведення масиву нових чисел
print("Піднесені до степеня числа:\n", arr, sep='')

