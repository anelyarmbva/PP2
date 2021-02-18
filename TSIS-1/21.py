def solve():
    n = int(input())
    m = int(input())
    for i in range(m):
        if i**2 in range(n, m + 1):
            print(i**2, end = ' ')
solve()  