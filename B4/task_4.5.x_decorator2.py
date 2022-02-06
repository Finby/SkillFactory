# decoratotr to show execution time
import time


def decorate_function(function_name):
    def wrapped(*args, **kwargs):
        result = function_name(*args, **kwargs)
        print(f'function {function_name} executed with result {result}')
        return result
    return wrapped


@decorate_function
def pow_2(n=9):
    return n ** 2


@decorate_function
def default_pow_2(n):
    return pow(n, 2)



print(pow_2(25) - default_pow_2(24))