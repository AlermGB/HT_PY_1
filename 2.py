# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = input('Input three digit number: ')
# print(int(number[0]) + int(number[1]) + int(number[2]))

# number = input('Input three digit number: ')
# sum_of_digits = 0
# for i in number:
#     sum_of_digits += int(i)
# print(f'Sum of digit of your number is {sum_of_digits}')

 
# def recursion_sum(num):
#     if num == 0: return 0
#     return recursion_sum(num // 10) + num % 10

# number = int(input('Input three digit number: '))
# print(recursion_sum(number))


number = int(input('Input three digit number: '))
sum_of_digits = number // 100 + (number - number // 100 * 100) // 10 + number % 10
print(f'Sum of digit of your number is {sum_of_digits}')
