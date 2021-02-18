n = int(input())
bool = False
for i in range(n):
    m = int(input())
    if m == 0:
        bool = True
if bool:
    print('YES')
else:
    print('NO')