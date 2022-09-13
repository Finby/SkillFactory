# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
# Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент функции,
# по значению результат работы функции, например, {n: f(n)}.
#
# И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
# То есть словарь можно считать промежуточной памятью на время работы программы,
# где будут храниться ранее вычисленные значения. Исходная функция, которую нужно задекорировать
# имеет следующий вид и выполняет простое умножение на число 123456789.:


def hashing_decorator(function_name):
    function_dict = {}

    def wrapped(m):
        nonlocal function_dict
        if m in function_dict:
            result = function_dict[m]
            print(f'function {function_name} with arg {m} is TAKEN from dictionary')
        else:
            result = function_name(m)
            function_dict[m] = result
            print(f'function {function_name} with arg {m} is added to dictionary')
        return result
    return wrapped


@hashing_decorator
def f(n):
    return n * 123456789


print(f(10))
print(f(11))
print(f(11))
print(f(10))
