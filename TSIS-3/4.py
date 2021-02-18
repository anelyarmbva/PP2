list = [int(i) for i in input().split()]
a = []
for i in list:
    if i != 0:
        a.append(i)
for i in range(len(list) - len(a)):
    a.append(0)
print(*a)