n = int(input())
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in range(n):
    m = int(input())
    if m == 0:
        cnt1 += 1
    elif m > 0:
        cnt2 += 1
    elif m < 0:
        cnt3 += 1
print(cnt1, cnt2, cnt3, sep = ' ')