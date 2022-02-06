def revers_stairs(max_high):
    if max_high <= 0:
        pass
    for i in range(max_high,0,-1):
        print("*" * i)
    print('----')


print(revers_stairs(int(input('enter number: '))))
