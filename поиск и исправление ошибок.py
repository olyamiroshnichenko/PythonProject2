# debug.py

# Фрагмент А
first = "2"
second = "3"

print("Фрагмент А:")
print("До:", type(first), type(second))

first = int(first)
second = int(second)

print("После:", type(first), type(second))
print("Результат:", first + second)

# Фрагмент Б
age = input("Возраст: ")

print("Фрагмент Б:")
print("До:", type(age))

age = int(age)

print("После:", type(age))
print("Возраст через год:", age + 1)

# Фрагмент В
first = 4
second = 7
third = 10

average = (first + second + third) / 3

print("Фрагмент В:")
print("Среднее:", average)

#Что было исправлено:

#Фрагмент А:
#"2" и "3" являются строками, поэтому "2" + "3" даёт 23.
#Преобразовали их в int, поэтому получаем:
#2 + 3 = 5

#Фрагмент Б:
#input() всегда возвращает строку (str). Поэтому перед сложением нужно сделать:
#age = int(age)
#Для ввода 17 результат будет:
#Возраст через год: 18

#Фрагмент В:
#Было просто сложение трёх чисел. Для среднего нужно разделить сумму на 3:
#average = (first + second + third) / 3
#Результат:
#7.0