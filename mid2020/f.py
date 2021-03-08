a, b = (int(i) for i in input().split())
cnt = 1

while (a * 3) <= (b * 2):
    cnt += 1
    a = a * 3
    b = b * 2

print(cnt)