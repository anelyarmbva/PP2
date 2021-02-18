list = [int(i) for i in input().split()]
k = int(input()) % len(list)
print(*(list[-k:] + list[:-k]))