input()
a={str(i) for i in input().split()}
input()
b={str(i) for i in input().split()}
a_b  = a.intersection(b)
a_b1 = a.difference(a_b)
a_b2 = b.difference(a_b)

a1 = list(a_b1)
a1.sort()
a2 = list(a_b2)
a2.sort()

print("Missed students:")
for x in a1:
  print("- " + x)
print("Not in the group:")
for x in a2:
  print("- " + x)