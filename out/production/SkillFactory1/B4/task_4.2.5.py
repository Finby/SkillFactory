def number_dividers(number_to_check: int) -> list:
    result = []
    for i in range(1, number_to_check // 2 + 1):
        if number_to_check % i == 0:
            result.append(i)
    result.append(number_to_check)
    return result


dividers = number_dividers(int(input('enter number: ')))
print(len(dividers))
print(*dividers, sep='\n')
