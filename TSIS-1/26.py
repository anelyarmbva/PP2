num = int(input())
i = 2
while i < num:
    if num % i == 0:
        print(i, end = ' ')
        break
    else:
        i += 1