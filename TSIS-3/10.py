n = int(input())
q = {}
for i in range(n):
    s1, s2 = map(str, input().split())
    q[s1] = s2
    q[s2] = s1
v = input()
print(q[v])