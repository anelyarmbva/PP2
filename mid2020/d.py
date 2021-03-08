txt = input()
x , y = 0, 0 
x1, y1 = (int(i) for i in input().split())

for i in range(len(txt)):
    if txt[i] == 'L':
        x = x - 1
        if x == x1 and y == y1:
            print('Passed')
            break
    elif txt[i] == 'R':
        x = x + 1
        if x == x1 and y == y1:
            print('Passed')
            break
    elif txt[i] == 'U':
        y = y + 1
        if x == x1 and y == y1:
            print('Passed')
            break
    elif txt[i] == 'D':
        y = y - 1
        if x == x1 and y == y1:
            print('Passed')
            break
else: 
    print('Missed')

    # print(txt[i])