from re import *

tex = input()
t = input()
s = input()
f = input()
x = sub(t, s, tex)
print(x.count(f))
