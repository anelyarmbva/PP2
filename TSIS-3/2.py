list = [int(i) for i in input().split()]
min = 0
for i in range(0, len(list)):
    if list[i] > 0:
        min = list[i]
        break
for i in range(len(list)):
    if list[i] > 0 and list[i] < min:
        min = list[i]
print(min)