# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.


def count_calls(function_name):
    count = 0

    def wrapped(*args, **kwargs):
        nonlocal count
        count += 1
        result = function_name(*args, **kwargs)
        print(f'function {function_name} called {count} time with result {result} ')
        return result

    return wrapped


@count_calls
def mul_2_num(a,b):
    return a * b


@count_calls
def temp1():
    return 0


for i in range(2):
    for j in range(2):
        print(mul_2_num(i, j))

temp1()