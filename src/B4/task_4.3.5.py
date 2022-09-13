# Дано натуральное число N. Вычислите сумму его цифр.


def sum_of_digits(number: int) -> int:
    if number < 10:
        return number
    return number % 10 + sum_of_digits(number // 10)


print(sum_of_digits(123))