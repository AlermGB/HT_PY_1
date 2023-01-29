# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

overall_result = int(input('How many cranes are done? '))
boy_result = int(overall_result / 6)
girl_result = int(boy_result * 4)
if overall_result % 6 == 0:
        print('Results of Petya, Katya, Seryoga are:')
        print(f'{boy_result} {girl_result} {boy_result}')
else:
    print('Your data are wrong!')
