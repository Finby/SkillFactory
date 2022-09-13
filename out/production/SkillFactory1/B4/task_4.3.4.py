# С помощью рекурсивной функции развернуть строку.


def recurs_reverse_string(s: str) -> str:
    if len(s) == 0:
        return ''
    return recurs_reverse_string(s[1:])+s[0]


print(recurs_reverse_string('1234'))