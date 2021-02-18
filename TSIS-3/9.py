n, m = map(int, input().split())
s1, s2 = set(), set()
for i in range(n):
    s1.add(int(input()))
for i in range(m):
    s2.add(int(input()))
a1, a2, a3 = s1 & s2, s1 - s2, s2 - s1
b1, b2, b3 = [i for i in a1], [i for i in a2], [i for i in a3]
b1.sort()
b2.sort()
b3.sort()
print(len(b1))
print(*(b1))
print(len(b2))
print(*(b2))
print(len(b3))
print(*(b3))
