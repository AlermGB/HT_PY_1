# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

bar_lenght = int(
    input('How many slices are in the length of your chocolate bar? '))
bar_width = int(
    input('How many slices are in the width of your chocolate bar? '))
check_number = int(input(
    'How many slices do you want to check for one-step-breakablility :)? '))
if (check_number % bar_lenght == 0 or check_number % bar_width == 0) and check_number < bar_lenght * bar_width:
    print("Yes. It's posible.")
else:
    print("No. It's imposible.")
