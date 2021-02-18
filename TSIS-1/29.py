from math import *
s = input()

cnt = 0

for i in len(s):
    if s[i] == ' ':
        cnt += 1
print(cnt)