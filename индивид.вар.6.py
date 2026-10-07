pizza_price = float(input("Введите цену пиццы: "))
pizza_count = int(input("Введите количество пицц: "))

drink_price = float(input("Введите цену напитка: "))
drink_count = int(input("Введите количество напитков: "))

pizza_total = pizza_price * pizza_count
drink_total = drink_price * drink_count
total = pizza_total + drink_total

print("Стоимость пиццы:", pizza_total)
print("Стоимость напитков:", drink_total)
print("Итоговая стоимость заказа:", total)

#вводим:
#360
#4
#200
#6
#выводит:
#Стоимость пиццы: 1440.0
#Стоимость напитков: 1200.0
#Итоговая стоимость заказа: 2640.0