# Создайте генератор, который по переданному списку создаёт последовательность,
# в которой элементы этого списка бесконечно циклично повторяются.
# Например, для списка [1, 2, 3] генератор создаст бесконечную последовательность 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, .


def cycle_list(my_list: list, limit =10):
    n = len(my_list)
    i = 0
    number = 0
    limit = (2 * n) if limit is None else limit
    while number < limit:
        yield my_list[i]
        i += 1
        i %= n
        number += 1


def cycle_list_2(my_list: list, limit =10):
    list_t = my_list.copy()
    for i in range(limit):
        value = list_t.pop(0)
        yield value
        list_t.append(value)


d = cycle_list_2
print(type(d))

# for i in cycle_list_2([1,3,3, 1000], 13):
#     print(i)