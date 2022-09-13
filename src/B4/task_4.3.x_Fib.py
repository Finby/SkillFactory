def my_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return my_fib(n-1) + my_fib(n-2)


def my_fib_generator(n=100):
    a, b = 0, 1
    yield a
    yield b
    i = 2
    while i <= n:
        a, b = b, a + b
        yield b
        i += 1


# print(my_fib(10))
for i in my_fib_generator(15):
    print(i)

for j in my_fib_generator(15):
    print(j)