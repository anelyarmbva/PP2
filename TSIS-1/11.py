from random import 
year = int(input())
a = year % 10
b = (year % 100) // 10
c = (year % 1000) // 1000
d = (year % 10000) // 10000
if a == d and b == c:
    print(1)
else:
    rand
