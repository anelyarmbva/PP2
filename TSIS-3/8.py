s1 = set(int(i) for i in input().split())
s2 = set(int(i) for i in input().split())
s3 = s1 & s2
a = []
for i in s3:
    a.append(i)
a.sort()
print(*a)
