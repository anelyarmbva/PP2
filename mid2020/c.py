n = int(input())

m = set(int(i) for i in input().split())
if n != len(m):
    print('NO')
else:
    print('YES')