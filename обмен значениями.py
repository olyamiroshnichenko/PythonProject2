# swap.py

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print()
print("До обмена:")
print("first_room  =", first_room)
print("second_room =", second_room)

# Обмен значениями через третью переменную
temp = first_room
first_room = second_room
second_room = temp

print()
print("После обмена:")
print("first_room  =", first_room)
print("second_room =", second_room)

#вводим:
#264
#245
#выводит:
#Первая аудитория: 264
#Вторая аудитория: 245

#До обмена:
#first_room  = 264
#second_room = 245

#После обмена:
#first_room  = 245
#second_room = 264