n = int(input())
a = input().split()
k = int(input())

x = a[0]
for i in range(1, k):
    x = (x * 1) + a[i]

y = a[k]
for i in range(k + 1, n):
    y = y * 1 + a[i]

print(int(x) * int(y))
# print(x)
# print(y)