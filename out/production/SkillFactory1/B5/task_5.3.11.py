# Напишите программу, которая на вход принимает последовательность целых чисел,
# и возвращает True, если все числа ненулевые,
# и False, если хотя бы одно число равно 0.


my_list = map(int, input().split())
print(type(my_list))
my_bool_list = [i != 0 for i in my_list]
print(all(my_bool_list))
