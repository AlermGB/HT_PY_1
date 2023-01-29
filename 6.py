# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticket_number = input('Input number of your ticket : ')
happy_sum_left = int(ticket_number[0]) + \
    int(ticket_number[1]) + int(ticket_number[2])
happy_sum_right = int(ticket_number[3]) + \
    int(ticket_number[4]) + int(ticket_number[5])
if happy_sum_left == happy_sum_right:
    print("Yes. It's happy.")
else: print("No. It isn't happy")
