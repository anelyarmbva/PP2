st = input().split()
max = len(st[0])
word = st[0]

for i in range(1, len(st)):
    if max < len(st[i]):
        max = len(st[i])
        word = st[i]

print(word)
print(max)
