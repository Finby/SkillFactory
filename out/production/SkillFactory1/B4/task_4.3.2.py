def multiply_function(*args):
    res = 1
    for i in args:
        res *= i
    return res


t = (1, 2, 3, 4, 5, 6)
print(multiply_function(*t))